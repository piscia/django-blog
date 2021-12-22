from django.contrib import admin
from blogging.models import Post, Category

# admin.site.register(Post)
# admin.site.register(Category)

class CategoryInline(admin.StackedInline):
    model = Category
    #exclude = ('posts',)

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
        ]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)