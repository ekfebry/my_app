# Generated by Django 4.2.6 on 2023-11-23 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_produk_keterangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='beranda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.beranda'),
            preserve_default=False,
        ),
    ]
