# Generated by Django 4.0.6 on 2022-11-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='nicho_mercado',
            field=models.CharField(choices=[('M', 'Marketing'), ('N', 'Nutrição'), ('D', 'Design'), ('T', 'Tecnologia')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]