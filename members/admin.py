from django.contrib import admin
from.models import Post,Account

# Register your models here.

@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status')
    list_filter = ('status','created','publish','auther')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('auther',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    list_editable = ('slug',)
    list_display_links = ('status',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('phone',)