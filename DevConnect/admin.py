from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):

    # 詳細画面: 表示項目
    basic = ("user_id", "user_name", "password")
    auth = ("is_admin",)

    fieldsets = (
        ("BasicInfo", {"fields": basic}),
        ("Auth", {"fields": auth}),
    )


admin.site.register(CustomUser, CustomUserAdmin)