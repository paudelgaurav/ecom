# Generated by Django 3.1.5 on 2021-01-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_order_used_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='place',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=12345, max_length=20),
            preserve_default=False,
        ),
    ]
