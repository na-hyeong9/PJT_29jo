# Generated by Django 3.2.13 on 2022-11-04 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('product_image', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('product_likes', models.ManyToManyField(related_name='like_products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review_image', imagekit.models.fields.ProcessedImageField(upload_to='media/')),
                ('grade_durability', models.FloatField()),
                ('grade_price', models.FloatField()),
                ('grade_design', models.FloatField()),
                ('grade_practicality', models.FloatField()),
                ('grade_avg', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('review_likes', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
