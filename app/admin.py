from django.contrib import admin
from .models import Notes,Todo

class NotesAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')
	search_fields = ('title',)
	list_per_page = 30


class TodoAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at')
	search_fields = ('title',)
	list_per_page = 30


admin.site.register(Notes, NotesAdmin)
admin.site.register(Todo, TodoAdmin)
