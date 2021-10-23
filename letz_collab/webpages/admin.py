from django.contrib import admin
from .models import HomepageBanner
from .models import TeamMembers
from django.utils.html import format_html


class TeamMembersAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'position', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'position')
    list_filter = ('position', 'created_at')


# Register your models here.
admin.site.register(HomepageBanner)
admin.site.register(TeamMembers, TeamMembersAdmin)
