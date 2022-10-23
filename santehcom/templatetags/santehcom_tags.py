from django import template
from santehcom.models import *
from santehcom.views import LoginUser

register = template.Library()


@register.simple_tag()
def get_products():
    return Products.objects.all()


@register.simple_tag()
def get_subcategories():
    return Subcategory.objects.all()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

# @register.inclusion_tag('products/login_form.html')
# def get_login():
#     login = LoginUser.as_view()
#     return {'login': login}