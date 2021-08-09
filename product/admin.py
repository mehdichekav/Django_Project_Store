from django.contrib import admin
from .models import Category, Product, Discount


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    actions = ('make_available',)

    def make_available(self, request, queryset):
        rows = queryset.update(available=True)
        self.message_user(request, f"{rows} updated")

    make_available.short_description = 'make all available'

    admin.site.add_action(make_available)


# @admin.register(Discount)
# class DiscountAdmin(admin.ModelAdmin):
#     list_display = ('title', 'cash', 'Deduction_from_the_price', 'description')
#     list_editable = ('Cash', 'Deduction_from_the_price')
admin.site.register(Discount)
