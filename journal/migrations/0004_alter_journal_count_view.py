# Generated by Django 4.2.5 on 2023-10-15 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0003_alter_journal_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='count_view',
            field=models.PositiveIntegerField(default=0, verbose_name='количество просмотров'),
        ),
    ]
