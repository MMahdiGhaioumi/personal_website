from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin, TabularInline
from contact import models

class SocialMediaTabular(TabularInline):
    model = models.SocialMedia
    extra = 0
    classes = ["collapse"]


class PhoneTabular(TabularInline):
    model = models.Phone
    extra = 0
    classes = ["collapse"]


class AddressTabular(TabularInline):
    model = models.Address
    extra = 0
    classes = ["collapse"]


class EmailTabular(TabularInline):
    model = models.Email
    extra = 0
    classes = ["collapse"]


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin, ModelAdmin):

    list_display = ['username', 'first_name', 'last_name']
    search_fields = ['username', 'user__emails']
    filter_horizontal = []
    list_filter = []
    inlines = [
        SocialMediaTabular,
        PhoneTabular,
        EmailTabular,
        AddressTabular,
    ]

    fieldsets = [
        ("حساب کاربری", {
            "fields": [
                'username',
                'password',
                'is_admin',
            ]
        }),
        ("اطلاعات عمومی کاربر", {
            "fields": [
                ('first_name', 'last_name'),
                ('country', 'city'),
                'birth_date',
                'age',
                'image',
                'resume',
            ]
        }),
        ("توضیحات کوتاه و کامل درباره کاربر", {
            "fields": [
                'information',
                'short_information'
            ],
            'classes': ['collapse']
        }),
        ("توضحات درباره مهارت ها", {
            "fields": [
                'title_skills',
                'text_skills',
            ],
            'classes': ['collapse']
        }),
    ]

    add_fieldsets = [
        (None, {
            'fields': [
                'username',
                'password1',
                'password2',
            ]
        })
    ]

    def get_inlines(self, request, obj=None):
        if obj is None:
            return []
        return self.inlines


admin.site.unregister(Group)
admin.site.site_header = "مدیریت سایت شخصی"
admin.site.index_title = "مدیریت سایت"
admin.site.site_title = "مدیریت سایت"
