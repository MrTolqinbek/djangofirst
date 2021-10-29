# Generated by Django 3.2.4 on 2021-10-29 09:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
