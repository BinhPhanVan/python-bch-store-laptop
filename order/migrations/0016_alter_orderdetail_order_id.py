# Generated by Django 4.0.4 on 2022-06-20 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_orderdetail_pro_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order'),
        ),
    ]
