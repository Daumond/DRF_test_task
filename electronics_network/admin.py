from django.contrib import admin
from .models import NetworkNode, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'debt', 'created_at')
    search_fields = ('name', 'city',)
    list_filter = ('city',)
    inlines = [ProductInline]
    actions = ['clear_debt']
    readonly_fields = ['created_at']

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)
    clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
