from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    def blurb(self, post):
        output = post.post_text[:100]
        if len(post.post_text) > 100:
            output += '...'
        return output

    blurb.short_description = 'Post Text'

    fields = ['post_title', 'post_text', 'post_image']
    list_display = ['post_title', 'blurb', 'post_date']
    list_filter = ['post_date']


admin.site.register(Post, PostAdmin)
