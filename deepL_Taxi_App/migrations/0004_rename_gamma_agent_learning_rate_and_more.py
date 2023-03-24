# Generated by Django 4.1.3 on 2022-12-06 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepL_Taxi_App', '0003_alter_agent_q'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='gamma',
            new_name='learning_rate',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='episode',
            new_name='sum_rewards',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='Q',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='alpha',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='nA',
        ),
        migrations.AddField(
            model_name='agent',
            name='avg_rewards',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='agent',
            name='decay_rate',
            field=models.FloatField(default=0.005),
        ),
        migrations.AddField(
            model_name='agent',
            name='discount_rate',
            field=models.FloatField(default=0.8),
        ),
        migrations.AddField(
            model_name='agent',
            name='max_steps',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='agent',
            name='num_episodes',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='agent',
            name='table',
            field=models.JSONField(default={}),
        ),
    ]
