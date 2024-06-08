# Generated by Django 4.2.13 on 2024-06-08 18:52

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainapps.accounts.models
import mainapps.common.validators
import mainapps.inventory.helpers.field_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=60, null=True)),
                ('picture', models.ImageField(default='default.png', null=True, upload_to='profile_pictures/%y/%m/%d/')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='not_to_mention', max_length=20, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_subscriber', models.BooleanField(default=False)),
                ('is_worker', models.BooleanField(default=False, editable=False)),
                ('is_main', models.BooleanField(default=False, editable=False)),
                ('date_of_birth', models.DateField(blank=True, help_text='You must be above 18 years of age.', null=True, validators=[mainapps.inventory.helpers.field_validators.adult_validator], verbose_name='Date Of Birth')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', mainapps.accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=6)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('time_requested', models.DateTimeField(auto_now=True)),
                ('successful_attempts', models.IntegerField(default=0)),
                ('total_attempts', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('code', 'message'), ('can_copy_code', 'Can copy code'), ('can_share_code', 'Can share code')),
            },
        ),
        migrations.CreateModel(
            name='ResidentialAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apt_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Apartment number')),
                ('street_number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Street number')),
                ('street', models.CharField(max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, help_text='Postal code', max_length=10, null=True, validators=[mainapps.common.validators.validate_postal_code], verbose_name='Postal code')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.city', verbose_name='City/Town')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.country', verbose_name='Country')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.region', verbose_name='Region/State')),
                ('resident', models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='residence', to=settings.AUTH_USER_MODEL)),
                ('subregion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.subregion', verbose_name='Sub region/LGA')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
