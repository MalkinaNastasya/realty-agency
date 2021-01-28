from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.utils.safestring import mark_safe

from .models import Customer, Owner, TypeRealty, Realty, RequestPurchase, ContractPurchase, AgencyRealtors, Realtors, \
    RealtorServices, ContractServices

@admin.register(Customer)
class Customer(ImportExportModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name",)

@admin.register(Owner)
class Owner(ImportExportModelAdmin):
    list_display = ("name", "phone", "email")
    search_fields = ("name",)

@admin.register(TypeRealty)
class TypeRealty(ImportExportModelAdmin):
    list_display = ("type_realty",)
    search_fields = ("type_realty",)

@admin.register(Realty)
class Realty(ImportExportModelAdmin):
    list_display = ("title", "description", "image", "address", "price")
    search_fields = ("title",)

def make_status_success(modeladmin, request, queryset):
    queryset.update(status='success')
make_status_success.short_description = "Сделка завершилась успешно"

def make_status_rejected(modeladmin, request, queryset):
    queryset.update(status='rejected')
make_status_rejected.short_description = "Сделка была закрыта, не состоявшись"

def make_status_consideration(modeladmin, request, queryset):
    queryset.update(status='consideration')
make_status_consideration.short_description = "Покупка на рассмотрении собственником"

@admin.register(RequestPurchase)
class RequestPurchase(ImportExportModelAdmin):
    list_display = ("title", "status")
    search_fields = ("title",)
    actions = [make_status_success, make_status_rejected, make_status_consideration]

@admin.register(ContractPurchase)
class ContractPurchase(ImportExportModelAdmin):
    list_display = ("title", "file")
    search_fields = ("title",)

@admin.register(AgencyRealtors)
class AgencyRealtors(ImportExportModelAdmin):
    list_display = ("name", "rating", "year_of_foundation")
    list_filter = ("year_of_foundation",)
    search_fields = ("title",)

@admin.register(Realtors)
class Realtors(ImportExportModelAdmin):
    list_display = ("name", "phone", "email", "rating")
    search_fields = ("name",)

@admin.register(RealtorServices)
class RealtorServices(ImportExportModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

@admin.register(ContractServices)
class ContractServices(ImportExportModelAdmin):
    list_display = ("title", "file")
    search_fields = ("title",)