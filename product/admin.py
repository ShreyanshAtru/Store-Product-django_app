from asyncio import format_helpers
from django.contrib import admin
from .models import Shop, Product, Category, Author
from django.utils.html import format_html
from .forms import AuthorForm

# Register your models here.

class AdminProduct(admin.ModelAdmin):

    def image_tag(self,obj):
        return format_html('<img src="{}" width="50" height="60" />'.format(obj.images.url))

    list_display = ['name', 'price', 'category','image_tag', 'active']
    search_fields = ['prod_ids','name',]
    list_filter = ('active','price',)
    list_display_links = ('name',)
    list_editable = ( 'price', 'category',)

    def get_queryset(self, request):
        queryset = super(AdminProduct, self).get_queryset(request)
        queryset = queryset.order_by('-prod_ids')
        return queryset


class AdminShop(admin.ModelAdmin):
    search_fields = ['title',]

class AdminCategory(admin.ModelAdmin):
    search_fields = ['product__name',]


admin.site.register(Shop, AdminShop)
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)



class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm

admin.site.register(Author, AuthorAdmin)