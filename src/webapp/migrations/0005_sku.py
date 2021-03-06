# Generated by Django 2.1.5 on 2019-02-07 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Product')),
            ],
            options={
                'verbose_name_plural': 'Stocks Keeping Units',
            },
        ),
    ]
