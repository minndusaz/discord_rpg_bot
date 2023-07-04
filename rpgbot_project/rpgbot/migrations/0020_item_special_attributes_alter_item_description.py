# Generated by Django 4.2.2 on 2023-07-04 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpgbot', '0019_item_attack_item_defense_item_health_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='special_attributes',
            field=models.JSONField(blank=True, default=dict, null=True, verbose_name='speccial_attributes'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]
