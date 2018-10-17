# Generated by Django 2.1.2 on 2018-10-17 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=200)),
                ('news_content', models.TextField()),
                ('news_time_publish', models.DateTimeField(verbose_name='news date published')),
                ('news_language', models.CharField(max_length=2)),
                ('news_domain', models.CharField(max_length=50)),
                ('news_date_download', models.DateTimeField(verbose_name='news date download')),
                ('news_url', models.CharField(max_length=300)),
                ('news_deletion', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='News_Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30)),
                ('author_fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getnewsurl.News')),
            ],
        ),
        migrations.CreateModel(
            name='News_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=300)),
                ('image_description', models.CharField(max_length=200)),
                ('image_stance', models.CharField(max_length=20)),
                ('image_fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getnewsurl.News')),
            ],
        ),
        migrations.CreateModel(
            name='News_Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_url', models.CharField(max_length=300)),
                ('movie_description', models.CharField(max_length=200)),
                ('movie_stance', models.CharField(max_length=20)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getnewsurl.News')),
            ],
        ),
        migrations.CreateModel(
            name='News_Stance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_stance', models.CharField(max_length=10)),
                ('news_true_language', models.CharField(max_length=2)),
                ('news_fkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='getnewsurl.News')),
            ],
        ),
    ]
