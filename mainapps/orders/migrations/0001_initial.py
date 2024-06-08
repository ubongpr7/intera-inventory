# Generated by Django 5.0.4 on 2024-05-09 12:24

import django.db.models.deletion
import mainapps.inventory.helpers.field_validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveBigIntegerField(blank=True, help_text='Total price for this order', null=True, verbose_name='Total Price')),
                ('order_currency', models.CharField(blank=True, help_text='Currency for this order (leave blank to use company default)', max_length=3, null=True, validators=[mainapps.inventory.helpers.field_validators.validate_currency_code], verbose_name='Order Currency')),
                ('description', models.CharField(blank=True, help_text='Order description (optional)', max_length=250, verbose_name='Description')),
                ('link', models.URLField(blank=True, help_text='Link to an external page', verbose_name='Link')),
                ('target_date', models.DateField(blank=True, help_text='Expected date for order delivery. Order will be overdue after this date.', null=True, verbose_name='Target Date')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='Creation Date')),
                ('reference', models.CharField(help_text='Order reference', max_length=64, unique=True, verbose_name='Reference')),
                ('status', models.PositiveIntegerField(choices=[(10, 'Pending'), (20, 'Placed'), (30, 'Complete'), (40, 'Cancelled'), (50, 'Lost'), (60, 'Returned')], default=10, help_text='Purchase order status')),
                ('supplier_reference', models.CharField(blank=True, help_text='Supplier order reference code', max_length=64, null=True, verbose_name='Supplier Reference')),
                ('issue_date', models.DateField(blank=True, help_text='Date order was issued', null=True, verbose_name='Issue Date')),
                ('complete_date', models.DateField(blank=True, help_text='Date order was completed', null=True, verbose_name='Completion Date')),
                ('address', models.ForeignKey(blank=True, help_text='Company address for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.address', verbose_name='Address')),
                ('contact', models.ForeignKey(blank=True, help_text='Point of contact for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.contact', verbose_name='Contact')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('received_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_purchase_orders', to=settings.AUTH_USER_MODEL, verbose_name='Received by')),
                ('responsible', models.ForeignKey(blank=True, help_text='User or group responsible for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Responsible')),
                ('supplier', models.ForeignKey(help_text='Company from which the items are being ordered', limit_choices_to={'is_supplier': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.company', verbose_name='Supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReturnOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveBigIntegerField(blank=True, help_text='Total price for this order', null=True, verbose_name='Total Price')),
                ('order_currency', models.CharField(blank=True, help_text='Currency for this order (leave blank to use company default)', max_length=3, null=True, validators=[mainapps.inventory.helpers.field_validators.validate_currency_code], verbose_name='Order Currency')),
                ('description', models.CharField(blank=True, help_text='Order description (optional)', max_length=250, verbose_name='Description')),
                ('link', models.URLField(blank=True, help_text='Link to an external page', verbose_name='Link')),
                ('target_date', models.DateField(blank=True, help_text='Expected date for order delivery. Order will be overdue after this date.', null=True, verbose_name='Target Date')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='Creation Date')),
                ('reference', models.CharField(help_text='Return Order reference', max_length=64, unique=True, verbose_name='Reference')),
                ('status', models.PositiveIntegerField(choices=[(10, 'Pending'), (20, 'In Progress'), (30, 'Complete'), (40, 'Cancelled')], default=10, help_text='Return order status', verbose_name='Status')),
                ('customer_reference', models.CharField(blank=True, help_text='Customer order reference code', max_length=64, verbose_name='Customer Reference ')),
                ('issue_date', models.DateField(blank=True, help_text='Date order was issued', null=True, verbose_name='Issue Date')),
                ('complete_date', models.DateField(blank=True, help_text='Date order was completed', null=True, verbose_name='Completion Date')),
                ('address', models.ForeignKey(blank=True, help_text='Company address for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.address', verbose_name='Address')),
                ('contact', models.ForeignKey(blank=True, help_text='Point of contact for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.contact', verbose_name='Contact')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('customer', models.ForeignKey(help_text='Company from which items are being returned', limit_choices_to={'is_customer': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.company', verbose_name='Customer')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('responsible', models.ForeignKey(blank=True, help_text='User or group responsible for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Responsible')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveBigIntegerField(blank=True, help_text='Total price for this order', null=True, verbose_name='Total Price')),
                ('order_currency', models.CharField(blank=True, help_text='Currency for this order (leave blank to use company default)', max_length=3, null=True, validators=[mainapps.inventory.helpers.field_validators.validate_currency_code], verbose_name='Order Currency')),
                ('description', models.CharField(blank=True, help_text='Order description (optional)', max_length=250, verbose_name='Description')),
                ('link', models.URLField(blank=True, help_text='Link to an external page', verbose_name='Link')),
                ('target_date', models.DateField(blank=True, help_text='Expected date for order delivery. Order will be overdue after this date.', null=True, verbose_name='Target Date')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='Creation Date')),
                ('customer_reference', models.CharField(blank=True, help_text='Customer order reference code', max_length=64, verbose_name='Customer Reference ')),
                ('shipment_date', models.DateField(blank=True, null=True, verbose_name='Shipment Date')),
                ('address', models.ForeignKey(blank=True, help_text='Company address for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.address', verbose_name='Address')),
                ('contact', models.ForeignKey(blank=True, help_text='Point of contact for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.contact', verbose_name='Contact')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('responsible', models.ForeignKey(blank=True, help_text='User or group responsible for this order', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Responsible')),
                ('shipped_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipped_sales', to=settings.AUTH_USER_MODEL, verbose_name='shipped by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalesOrderShipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_date', models.DateField(blank=True, help_text='Date of shipment', null=True, verbose_name='Shipment Date')),
                ('delivery_date', models.DateField(blank=True, help_text='Date of delivery of shipment', null=True, verbose_name='Delivery Date')),
                ('reference', models.CharField(default='1', help_text='Shipment number', max_length=100, verbose_name='Shipment')),
                ('tracking_number', models.CharField(blank=True, help_text='Shipment tracking information', max_length=100, verbose_name='Tracking Number')),
                ('invoice_number', models.CharField(blank=True, help_text='Reference number for associated invoice', max_length=100, verbose_name='Invoice Number')),
                ('link', models.URLField(blank=True, help_text='Link to external page', verbose_name='Link')),
                ('checked_by', models.ForeignKey(blank=True, help_text='User who checked this shipment', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Checked By')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('order', models.ForeignKey(help_text='Sales Order', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='orders.salesorder', verbose_name='Order')),
            ],
            options={
                'unique_together': {('order', 'reference')},
            },
        ),
    ]