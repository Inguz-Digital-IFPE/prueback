# Generated by Django 4.2 on 2023-08-24 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Uprofile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=128, null=True)),
                ('curp', models.CharField(blank=True, max_length=64, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]