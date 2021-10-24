from django.contrib import admin

from .models import Youtuber


class YoutuberAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'price', 'category',
                    'country', 'is_featured', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'country', 'category')
    list_filter = ('country', 'category', 'created_at')
    list_editable = ('is_featured',)


# Register your models here.
admin.site.register(Youtuber, YoutuberAdmin)
