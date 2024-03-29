# Generated by Django 2.2.3 on 2019-09-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190906_1019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='comments_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
