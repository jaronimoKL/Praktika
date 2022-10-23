from PIL import Image
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import date

from django.urls import reverse


class Products(models.Model):
    # Товары
    name = models.CharField("Товар", max_length=150, db_index=True)
    description = models.TextField("Описание", blank=True)
    article = models.CharField("Артикуль", max_length=11)
    price = models.DecimalField("Цена", max_digits=19, decimal_places=2, help_text="указывать в рублях")
    slug = models.SlugField(max_length=200, db_index=True, default='')
    stock = models.PositiveSmallIntegerField("Количество товаров", default=0)
    available = models.BooleanField(default=True)
    event = models.BooleanField("Акция")
    percentage_event = models.IntegerField("Процент акции", blank=True, null=True)
    created = models.DateField("Дата появления товара", default=date.today)
    popular = models.BooleanField("Популярное")
    image = models.ImageField("Изображение", upload_to="products/%Y/%m/")
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, verbose_name='Подкатегория')
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Бренд')
    rate = models.ForeignKey('Rating', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Оценка')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='profile_images/default.jpg', upload_to='profile_images/')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Favourite(models.Model):
    # Избранное
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.product} - {self.user}"

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"


class Brand(models.Model):
    # Бренд
    name = models.CharField("Название бренда", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Category(models.Model):
    # Категории
    name = models.CharField("Название категории", max_length=50)
    image = models.ImageField("Изображение, представляющее категорию", upload_to="category/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    # Подкатегории
    name = models.CharField("Название подкатегории", max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Score(models.Model):
    # Оценка
    number = models.PositiveSmallIntegerField("Оценка", default=0)
    img = models.FileField("Изображение кол-ва звёзд", upload_to="stars/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"


class Crate(models.Model):
    # Корзина
    amount = models.PositiveSmallIntegerField("Количество товаров", default=0)
    price = models.PositiveIntegerField("Цена товара", default=0)
    sum = models.PositiveBigIntegerField("Сумма цены товаров", default=0)
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return f"{self.user} - {self.product}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Rating(models.Model):
    # Рейтинг
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    score = models.ForeignKey('Score', on_delete=models.CASCADE, verbose_name='Оценка')
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return f"{self.user} - {self.product} - оценка - {self.score}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
