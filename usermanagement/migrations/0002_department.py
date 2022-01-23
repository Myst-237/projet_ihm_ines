# Generated by Django 3.2.9 on 2022-01-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MG', 'Medicine General'), ('CA', 'Cardiologie'), ('CH', 'Chirurgi'), ('MA', 'Maternite'), ('UR', 'Urgence'), ('RA', 'Radiologie'), ('PE', 'Pediatrie')], max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
    ]
