# Generated by Django 5.1.4 on 2024-12-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('work_experience', models.TextField()),
                ('service_category', models.CharField(max_length=255)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='Группы, к которым принадлежит пользователь.', related_name='customuser_groups', to='auth.group', verbose_name='группы')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Права доступа пользователя.', related_name='customuser_permissions', to='auth.permission', verbose_name='права доступа')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
