
USER_ROLES = [
    # TODO: due to security issues remove admin choice later and handle using django is_admin and is_staff fields
    ('farmer', 'Farmer'),
    ('merchant', 'Merchant'),
    ('admin', 'Admin')
]
PRODUCT_CATEGORY_CHOICES = [
    ('livestock', 'Liverstock'),
    ('machinery', 'Merchinery'),
    ('foodstuff', 'FoodStuff')
]
PRODUCT_FILE_TYPE = [
    ('VD', 'Video'),
    ('PP', 'Picture')
]
ORDER_STATUS_CHOICES = [
    ('pending', 'pending'),
    ('success', 'success'),
    ('declined', 'declined')

]
