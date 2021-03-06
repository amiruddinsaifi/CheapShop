# Generated by Django 2.2.3 on 2019-08-08 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contect',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(default='', max_length=100)),
                ('phone', models.IntegerField(default='', max_length=10)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
