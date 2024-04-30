from django.contrib import admin

from app.models import Function, Ministry, Scale, User

class UserAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name",
                    "email",
                    "function",
                    "ministry",
                    "created_at",
                    "updated_at"
    ]

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Ministry)
admin.site.register(Function)
admin.site.register(Scale)