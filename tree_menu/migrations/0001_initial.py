# Generated by Django 4.2.7 on 2023-11-02 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Меню')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Element_submenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Элемент подменю')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='URL')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tree_menu.tree_menu', verbose_name='id меню')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='tree_menu.element_submenu', verbose_name='родитель')),
            ],
            options={
                'verbose_name': 'Элемент меню',
                'verbose_name_plural': 'Элементы меню',
            },
        ),
    ]
