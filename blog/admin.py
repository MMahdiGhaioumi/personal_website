from django.contrib import admin
from . import models


class CommentAdminSack(admin.StackedInline):
    model = models.Comment
    extra = 1
    classes = ['collapse']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
    inlines = [CommentAdminSack]
    search_fields = ["title", "body", "user__username"]
    list_per_page = 20
    list_max_show_all = 200
    autocomplete_fields = ['tags']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    list_editable = ('status',)
    search_fields = ['name', 'email']
    list_per_page = 20
    list_max_show_all = 200
    autocomplete_fields = ['post', 'parent']

    list_select_related = ['parent', 'post']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
