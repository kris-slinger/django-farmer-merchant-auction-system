import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from datetime import timedelta, date
from django.core.signals import  request_finished

@receiver(post_save, sender=Order, dispatch_uid="total_price")
def calculateOrderTotalPrice(sender,instance,**kwargs):
    total_price = instance.order_quantity*instance.order_price
    Order.objects.filter(order_id=instance.order_id).update(order_total_price=total_price)

@receiver(post_save, sender=Order, dispatch_uid="updateExpirationdate")
def updateOrderExpirationDate(sender, instance, **kwargs):
    # populate order_expiration_date=order_creation_date+7 days
    Order.objects.filter(order_id=instance.order_id).update(
        order_expiration_date=instance.order_creation_date + timedelta(days=7))

# TODO: confirm that order is deleted after 7 days
@receiver(request_finished, dispatch_uid="delete_if_expired")
def deleteOrderIfExpired(sender,**kwargs):
    query = Order.objects.filter(order_expiration_date=date.today())
    if query:
        query.delete()
