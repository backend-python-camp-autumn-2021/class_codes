from django.contrib import admin

from .models import Article, Author, User, Category, Comment, Personkheng, Group, Membership


class CommentInline(admin.StackedInline):
    model = Comment


class AuthorInline(admin.TabularInline):
    model = Author


class UserAdmin(admin.ModelAdmin):
    inlines = [
        AuthorInline,
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['number_of_comments', ]
    list_display = ('title', 'author', 'abstract_context')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'context')
        }),
        ('Detail', {
            'fields': ('seen_num', 'category'),
        }),

    )
    inlines = [
        CommentInline,
    ]
    search_fields = ('title', 'context',)


# admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Personkheng)
admin.site.register(Group)
admin.site.register(Membership)
