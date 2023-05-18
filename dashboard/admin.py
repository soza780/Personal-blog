from django.contrib import admin
from .models import UserProfile, Transaction, UserSocialLinks


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("owner", "wallet",)
    search_fields = ("owner__email", "transcations__time",)


class TranscationAdmin(admin.ModelAdmin):
    list_display = ("time", "user", "amount",)
    search_fields = ("time", "user", "amount",)


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("owner",)
    search_fields = ("owner",)


admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(Transaction, TranscationAdmin)
admin.site.register(UserSocialLinks, SocialLinkAdmin)
