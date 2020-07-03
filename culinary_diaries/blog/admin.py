from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    def blurb(self, post):
        return post.post_text[:100]

    fields = ['post_title', 'post_text']
    blurb.short_description = 'Post Text'
    list_display = ['post_title', 'blurb', 'post_date']


admin.site.register(Post, PostAdmin)
