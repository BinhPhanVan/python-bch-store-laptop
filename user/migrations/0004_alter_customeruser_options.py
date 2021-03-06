# Generated by Django 4.0.4 on 2022-06-16 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customeruser_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customeruser',
            options={'permissions': [('can_view_category', 'can_view_category'), ('can_change_order', 'can_change_order'), ('can_view_product', 'can_view_product'), ('can_view_variation', 'can_view_variation'), ('can_change_user', 'can_change_user'), ('can_add_order', 'can_add_order'), ('can_delete_order', 'can_delete_order'), ('can_view_order', 'can_view_order'), ('can_add_cart', 'can_add_cart'), ('can_change_cart', 'can_change_cart'), ('can_delete_cart', 'can_delete_cart'), ('can_view_cart', 'can_view_cart'), ('can_add_cart_item', 'can_add_cart_item'), ('can_change_cart_item', 'can_change_cart_item'), ('can_delete_cart_item', 'can_delete_cart_item'), ('can_view_cart_item', 'can_view_cart_item')]},
        ),
    ]
