# Generated by Django 2.1.3 on 2018-11-12 18:59

from django.db import migrations, models
import django.db.models.deletion
import girls.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Girl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Last name')),
                ('date_of_birth', models.DateField(default=girls.models.default_date_of_birth, verbose_name='Date of birth')),
                ('hair_color', models.CharField(blank=True, max_length=30, null=True, verbose_name='Hair color')),
                ('height', models.IntegerField(blank=True, null=True)),
                ('parameters', models.CharField(blank=True, max_length=20, null=True, verbose_name='Parameters')),
                ('eye_color', models.CharField(blank=True, max_length=20, null=True, verbose_name='Eye color')),
                ('image_id', models.CharField(blank=True, max_length=256, null=True, verbose_name='Image id')),
                ('has_cover', models.BooleanField(default=False, verbose_name='Has cover')),
            ],
        ),
        migrations.CreateModel(
            name='ModelImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=girls.models.get_model_upload_path)),
                ('is_cover', models.BooleanField(default=False, verbose_name='Cover Image')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='girls.Girl')),
            ],
        ),
    ]
