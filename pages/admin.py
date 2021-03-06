from django.contrib import admin
from django.contrib import admin
from pages.models import NewsEntry
from pages.models import History

admin.site.register([ History])



'''
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }

    list_display = ('name', 'slug')
'''

class NewsEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }

    list_display = ('created_at', 'published_at', 'title', 'draft')
    list_display_links = ('title',)
    list_filter = ('created_at', 'published_at', 'draft')
    date_hierarchy = 'created_at'
    search_fields = ('title', 'tease', 'body')

    exclude = ('created_at',)
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'tease', 'body', 'image')}),
        ('Properties', {'fields': ('draft', 'published_at')}),
    )


'''
admin.site.register(Category, CategoryAdmin)
'''
admin.site.register(NewsEntry, NewsEntryAdmin)
