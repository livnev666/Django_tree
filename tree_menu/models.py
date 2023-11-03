from django.db import models

# Create your models here.


class Tree_Menu(models.Model):

    """Меню содержащее пункты подменю"""

    title = models.CharField(max_length=255, verbose_name='Меню')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True, blank=True, verbose_name='URL')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Element_submenu(models.Model):

    """Элемент меню"""

    title = models.CharField(max_length=255, verbose_name='Элемент подменю')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True, verbose_name='URL')

    menu = models.ForeignKey(Tree_Menu, on_delete=models.CASCADE, null=True, verbose_name='id меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True, verbose_name='родитель', related_name='childrens')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'



