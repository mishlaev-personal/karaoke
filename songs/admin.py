from django.contrib import admin
from .models import Song, Performer


class SongInLine(admin.TabularInline):
    model = Song


class PerformerAdmin(admin.ModelAdmin):
    inlines = [SongInLine, ]


admin.site.register(Performer, PerformerAdmin)
admin.site.register(Song)
