import datetime

from django.contrib import admin


from birds.models import PhotoGallery, Articles, FeedBackForm, Comment


#admin.site.register(Articles)
#admin.site.register(Comment)
#admin.site.register(FeedBackForm)
admin.site.register(PhotoGallery)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author_name', 'date_publicity', 'date_created', 'image', 'text', 'full_text')
    list_filter = ('date_publicity',)
    actions_on_bottom = True
    actions_on_top = False
    list_per_page = 3
    search_fields = ('title', 'text')

admin.site.register(Articles, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('note', 'date_of_send', 'author_name', 'email', 'comment')
    actions_on_bottom = True
    actions_on_top = False
    list_per_page = 3
    search_fields = ('note' ,'comment')

admin.site.register(Comment, CommentAdmin)

class FeedBackFormAdmin(admin.ModelAdmin):
    list_filter = ('status', )

admin.site.register(FeedBackForm, FeedBackFormAdmin)

