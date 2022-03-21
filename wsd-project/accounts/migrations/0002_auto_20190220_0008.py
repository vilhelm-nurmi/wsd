# Generated by Django 2.1.3 on 2019-02-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('accounts', '0001_initial'),
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='purchased_games',
            field=models.ManyToManyField(blank=True, to='games.Game'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
