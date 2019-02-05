# Generated by Django 2.1.5 on 2019-01-28 14:42

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
            name='Statya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=280, verbose_name='name stayi')),
                ('text', models.TextField(verbose_name='text statyi')),
                ('time', models.DateField(auto_now=True)),
                ('picture', models.ImageField(blank=True, upload_to='images/')),
                ('prosmotry', models.IntegerField(default=0)),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
