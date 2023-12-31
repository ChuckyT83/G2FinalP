# Generated by Django 4.2.7 on 2023-12-13 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_character_range_alter_character_support'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choiceEight',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='choiceNine',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answerFive',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answerSeven',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answerSix',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
