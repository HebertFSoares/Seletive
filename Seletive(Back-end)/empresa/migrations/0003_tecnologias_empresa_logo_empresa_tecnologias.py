# Generated by Django 4.0.6 on 2022-11-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_empresa_nicho_mercado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tecnologia', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo_empresa'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='tecnologias',
            field=models.ManyToManyField(to='empresa.tecnologias'),
        ),
    ]