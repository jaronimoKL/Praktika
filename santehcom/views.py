from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum, Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from santehcom.forms import *
from santehcom.models import *


menu = [
    {'title': "Номера", 'url_name': 'rooms'},
    {'title': "Услуги", 'url_name': 'service'},
    {'title': "Акции", 'url_name': 'stock'},
    {'title': "Отзывы", 'url_name': 'reviews'}
]


# Список товаров
def Product(reqeust):
    products = Products.objects.all()
    cats = Category.objects.all()

    context = {
        'product': products,
        'cats': cats,
        'title': 'Главная страница',
    }
    return render(reqeust, "products/product_list.html", context=context)


# Каталог товаров
def CatalogList(reqeust):
    products = Products.objects.filter(available=True)
    subcategory = Subcategory.objects.all()
    category = Category.objects.all()
    rate = Rating.objects.all()
    context = {
        "products": products,
        "rating": rate,
        "subcategory": subcategory,
        "category": category,
        'title': 'Каталог',
    }
    return render(reqeust, "products/catalog.html", context=context)


# Описание товара
def ProductDetail(request, slug):
    detail = get_object_or_404(Products, slug=slug)
    products = Products.objects.all()
    context = {
        'product': products,
        'detail': detail,
        'slug': slug,
        'title': products,
    }
    return render(request, "products/product.html", context=context)


#Слайдер
# def Recently(request, product_slug):
#     product = Products.objects.all()
#     product_slug = Products.slug
#     context = {
#         'product': product,
#         'slug': product_slug,
#     }
#     return render(request, "base.html", context=context)


#Список категорий
def Catalog(request):
    products = Products.objects.all()
    catalog_c = Category.objects.all()
    catalog_sc = Subcategory.objects.all()
    context = {
        'product': products,
        'category': catalog_c,
        'category_s': catalog_sc,
        'title': 'Список категорий',
    }
    return render(request, "products/catalog_list.html", context=context)


#Поиск товаров
class SearchListView(ListView):
    model = Products
    template_name = 'products/catalog_search.html'
    context_object_name = "results_objects"

    def get_queryset(self):
        query = self.request.GET.get('q')
        products = Products.objects.filter(
            Q(name__icontains=query) | Q(subcategory__name__icontains=query)
        )
        return products

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get('q')
        return context


#Страница контактов
def Contact(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'products/contact.html', context=context)


#Страница о компании
def About(request):
    context = {
        'title': 'О компании',
    }
    return render(request, 'products/about.html', context=context)


#Страница отзывов
def Feedback(request):
    context = {
        'title': 'Отзывы',
    }
    return render(request, 'products/feedback.html', context=context)


#В разработке
def Develop(request):
    context = {
        'title': 'В разработке',
    }
    return render(request, 'products/development.html', context=context)


#Регистрация
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'products/register_form.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


#Авторизация
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'products/login_form.html'

    def get_success_url(self):
        return reverse_lazy('main')


def LogoutUser(request):
    logout(request)
    return redirect('login')


@login_required
def ProfileUser(request):
    img = Profile.objects.all()

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'image': img,
        'title': 'Личный кабинет',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'products/profile.html', context=context)


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'products/profile_change-password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')


#Не найдено
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена''</h1>''<br>''<p>''Или находится в разработке''</p>')
