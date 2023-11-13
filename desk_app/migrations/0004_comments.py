# Generated by Django 4.2.6 on 2023-11-13 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('desk_app', '0003_alter_posts_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='desk_app.posts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]