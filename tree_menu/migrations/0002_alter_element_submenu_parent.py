# Generated by Django 4.2.7 on 2023-11-02 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element_submenu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='tree_menu.element_submenu', verbose_name='родитель'),
        ),
    ]
