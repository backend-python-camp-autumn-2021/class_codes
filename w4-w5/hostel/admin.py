from django.contrib import admin

from .models import HostelCategory, HostImage, HostAddress, Host, HostComment


class HostImageInline(admin.TabularInline):
    model = HostImage


class HostCommentInline(admin.TabularInline):
    model = HostComment


@admin.register(Host)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        HostImageInline,
        HostCommentInline
    ]