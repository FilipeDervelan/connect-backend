from django.contrib import admin

from app.models import CustomUser, Function, Ministry, Scale, Unavailability


class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "birth_day",
        "created_at",
        "updated_at",
    ]


class UnavailabilityAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "user",
        "start_date",
        "end_date",
        "created_at",
        "updated_at",
    ]


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ministry)
admin.site.register(Function)
admin.site.register(Scale)
admin.site.register(Unavailability, UnavailabilityAdmin)
