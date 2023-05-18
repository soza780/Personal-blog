from django.contrib import admin
from .models import UserProfile, Transaction


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("owner", "wallet",)
    search_fields = ("owner__email", "transcations__time",)


class TranscationAdmin(admin.ModelAdmin):
    list_display = ("time", "user", "amount",)
    search_fields = ("time", "user", "amount",)


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Transaction, TranscationAdmin)