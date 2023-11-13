# Generated by Django 4.2.6 on 2023-11-09 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desk_app', '0002_remove_posts_author_posts_categories_posts_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='desk_app.publisher'),
        ),
    ]
