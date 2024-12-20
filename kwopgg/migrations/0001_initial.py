# Generated by Django 5.1.3 on 2024-11-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassroomInfDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('capacity_max', models.IntegerField(blank=True, null=True)),
                ('reserved_time', models.DateTimeField(blank=True, null=True)),
                ('place_name', models.CharField(blank=True, max_length=100, null=True)),
                ('image_id', models.CharField(blank=True, max_length=50, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('has_mic', models.BooleanField(blank=True, null=True)),
                ('has_projector', models.BooleanField(blank=True, max_length=50, null=True)),
                ('building_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('reserved', models.BooleanField(blank=True, null=True)),
                ('desk_type', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'classroom_inf_dev',
            },
        ),
        migrations.CreateModel(
            name='ClassroomReviewDev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mic_status', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('clean_status', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('air_conditioner_status', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('size_satisfaction', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('place_name', models.CharField(blank=True, max_length=100, null=True)),
                ('building_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'classroom_review_dev',
            },
        ),
    ]
