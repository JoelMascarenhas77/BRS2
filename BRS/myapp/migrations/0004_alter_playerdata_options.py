# Generated by Django 4.0.5 on 2022-07-17 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_playerdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playerdata',
            options={'ordering': ['Rating', [-1]]},
        ),
    ]