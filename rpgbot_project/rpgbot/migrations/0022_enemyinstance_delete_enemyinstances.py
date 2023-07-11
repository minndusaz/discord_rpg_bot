# Generated by Django 4.2.2 on 2023-07-11 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpgbot', '0021_enemy_drops'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnemyInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_health', models.IntegerField(default=0, verbose_name='current_health')),
                ('enemy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enemy_instances', to='rpgbot.enemy', verbose_name='enemy')),
            ],
            options={
                'verbose_name': 'enemyInstances',
                'verbose_name_plural': 'enemyInstancess',
            },
        ),
        migrations.DeleteModel(
            name='EnemyInstances',
        ),
    ]
