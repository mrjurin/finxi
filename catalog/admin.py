from django.contrib import admin
from .models import RealEstate, Seller, State, Contact, Address, City


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]

    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']


class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('title', 'transactionType', 'type', 'sellPrice', 'rentPrice', 'sold', 'address', 'created_at')
    exclude = ('sold', 'sold_at')


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('code', 'number')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'number', 'city', 'postalCode')


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')


admin.site.register(RealEstate, RealEstateAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(City, CityAdmin)
