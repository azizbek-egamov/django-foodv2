from django.contrib import admin
from .models import *

class FoodAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return [field for field in fields if field != 'rand']

    list_display = ('nomi', 'narxi', 'rasm', 'holati', 'sana')

    def get_list_display(self, request):
        return [field for field in super().get_list_display(request) if field != 'rand']
    
@admin.register(Users)
class FoodAdmin2(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'phone')

admin.site.register(Food, FoodAdmin)

@admin.register(AdminId)
class Adminid(admin.ModelAdmin):
    list_display = ('admin',)
    
    def has_add_permission(self, request):
        if AdminId.objects.count() >= 1:
            return False
        else:
            return True
        
@admin.register(CardInfo)
class Adminid(admin.ModelAdmin):
    list_display = ('card_number', 'qr_kod')
    
    def has_add_permission(self, request):
        if CardInfo.objects.count() >= 1:
            return False
        else:
            return True