# Generated by Django 3.1 on 2020-08-14 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodThingThatHappened',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_happened', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goodthingthathappened_author', to=settings.AUTH_USER_MODEL)),
                ('who_its_about', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='goodthingthathappened_who_its_about', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
