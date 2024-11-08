# Generated by Django 5.1.1 on 2024-11-05 10:44

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('is_main', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=128)),
                ('fax', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ')),
                ('email', models.EmailField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OptionObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AppealStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('is_closed', models.BooleanField(default=False)),
                ('color', models.CharField(default='FFFFFF', max_length=16)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appeal_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AppealStatus',
                'verbose_name_plural': 'AppealStatuses',
            },
        ),
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=128, null=True)),
                ('call_status', models.CharField(blank=True, choices=[('interested', 'Interested'), ('not_interested', 'Not Interested'), ('do_not_distrub', 'Do Not Distrub'), ('callback', 'Callback'), ('information_left', 'Information Left')], max_length=23)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appeals', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appeals', to='telemarketing.appealstatus')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appeals', to='telemarketing.branch')),
            ],
            options={
                'ordering': ['-updaetd_at'],
            },
        ),
        migrations.CreateModel(
            name='CallScript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=23, unique=True)),
                ('module', models.CharField(choices=[('telemarketing', 'telemarketing'), ('contact_center', 'contact_center')], max_length=23)),
                ('text', models.TextField()),
                ('is_active', models.BooleanField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='call_scripts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Call Script',
                'verbose_name_plural': 'Call Scripts',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='channels', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Chouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('fullname', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('request_time', models.DateTimeField(blank=True, null=True)),
                ('fraud_type', models.CharField(blank=True, max_length=128, null=True)),
                ('stealing_info', models.TextField(blank=True, null=True)),
                ('fraudser_info', models.TextField(blank=True, null=True)),
                ('payment_service', models.TextField(blank=True, null=True)),
                ('owner_name', models.TextField(blank=True, null=True)),
                ('stolen_amount', models.FloatField(blank=True, null=True)),
                ('customer_card', models.TextField(blank=True, null=True)),
                ('rogue_address', models.TextField(blank=True, null=True)),
                ('scrammed_device_info', models.TextField(blank=True, null=True)),
                ('fraudcer_payment_info', models.TextField(blank=True, null=True)),
                ('scam_info', models.TextField(blank=True, null=True)),
                ('phishing_site', models.URLField(blank=True, null=True)),
                ('otp_code', models.IntegerField(blank=True, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chouses', to=settings.AUTH_USER_MODEL)),
                ('appeal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='telemarketing.appeal')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('type', models.CharField(max_length=128)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('appeal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='telemarketing.appeal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='text', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Credit',
                'verbose_name_plural': 'Credits',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=56, null=True)),
                ('passport', models.CharField(blank=True, max_length=9, null=True, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ')),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('famale', 'Famale')], max_length=6, null=True)),
                ('pnfl', models.CharField(blank=True, max_length=14, null=True)),
                ('level', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=6)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customers', to=settings.AUTH_USER_MODEL)),
                ('channel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customers', to='telemarketing.channel')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='appeal',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appeals', to='telemarketing.customer'),
        ),
        migrations.CreateModel(
            name='CustomerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CustomerCategory',
                'verbose_name_plural': 'CustomerCategories',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customers', to='telemarketing.customercategory'),
        ),
        migrations.CreateModel(
            name='CustomerStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_status', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CustomerStatus',
                'verbose_name_plural': 'CusomerStatuses',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customers', to='telemarketing.customerstatus'),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('functions', models.TextField(blank=True, null=True)),
                ('register_client', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='options0', to=settings.AUTH_USER_MODEL)),
                ('object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='options', to='telemarketing.optionobject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='appeal',
            name='options',
            field=models.ManyToManyField(blank=True, related_name='appeals', to='telemarketing.option'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('status', models.CharField(choices=[('calculator', 'calculator'), ('chouse', 'chouse'), ('text', 'text')], max_length=11)),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('product_url', models.CharField(blank=True, max_length=256, null=True)),
                ('iabsproduct_id', models.IntegerField(default=-1)),
                ('order_id', models.PositiveIntegerField(default=1)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to=settings.AUTH_USER_MODEL)),
                ('options', models.ManyToManyField(related_name='products', to='telemarketing.option')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='telemarketing.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('is_lead', models.BooleanField(default=False)),
                ('is_agrement', models.BooleanField(default=False)),
                ('is_visit', models.BooleanField(default=False)),
                ('is_scoring', models.BooleanField(default=False)),
                ('is_issuance', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processes', to=settings.AUTH_USER_MODEL)),
                ('appeal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processes', to='telemarketing.appeal')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='processes', to='telemarketing.branch')),
                ('products', models.ManyToManyField(related_name='processes', to='telemarketing.product')),
            ],
            options={
                'verbose_name': 'Process',
                'verbose_name_plural': 'Processes',
            },
        ),
        migrations.AddField(
            model_name='appeal',
            name='products',
            field=models.ManyToManyField(related_name='related_appeals', to='telemarketing.product'),
        ),
        migrations.CreateModel(
            name='ScriptCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='script_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=512)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scripts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scripts', to='telemarketing.scriptcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updaetd_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='types', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ManyToManyField(related_name='products', to='telemarketing.type'),
        ),
        migrations.AddField(
            model_name='appeal',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='appeals', to='telemarketing.type'),
        ),
    ]
