# Generated by Django 5.1.2 on 2024-12-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='blog_files/')),
            ],
            options={
                'ordering': ['create_at'],
            },
        ),
    ]
