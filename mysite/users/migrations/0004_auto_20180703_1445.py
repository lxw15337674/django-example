# Generated by Django 2.0.6 on 2018-07-03 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180628_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='graduate_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_join_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='job_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='team_belong',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zhengzhi_mianmao',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zhengzhi_time',
        ),
    ]
