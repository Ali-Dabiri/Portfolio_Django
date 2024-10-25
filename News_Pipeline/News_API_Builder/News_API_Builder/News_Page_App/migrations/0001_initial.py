# Generated by Django 5.1.2 on 2024-10-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=200)),
                ('news_content', models.CharField(max_length=200)),
                ('news_tag', models.TextField()),
                ('news_source', models.CharField(max_length=200)),
            ],
        ),
    ]