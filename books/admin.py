from django.contrib import admin

from books.models import Book, Image, Comment, Reply, Chapter, Tag, TagBook


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'description', 'author', 'status', 'is_vip')
    search_fields = ['title', 'author']
    raw_id_fields = []
    list_filter = ['is_vip', 'status', 'is_enable']


class ChaptersAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'title', 'like_count')
    search_fields = ['title']
    list_filter = ['book']


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'chapter', 'image')
    raw_id_fields = []
    search_fields = ['chapter']


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    raw_id_fields = []
    search_fields = ['name']


class TagBooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'book')
    raw_id_fields = []
    search_fields = ['tag']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'chapter', 'user', 'content', 'like_count')
    raw_id_fields = []
    search_fields = ['user', 'content']


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment', 'user', 'reply')
    raw_id_fields = []
    search_fields = ['comment', 'user', 'reply']


admin.site.register(Book, BooksAdmin)
admin.site.register(Chapter, ChaptersAdmin)
admin.site.register(Image, ImagesAdmin)
admin.site.register(Tag, TagsAdmin)
admin.site.register(TagBook, TagBooksAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Reply, ReplyAdmin)
