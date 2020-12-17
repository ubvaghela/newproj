from django.contrib import admin
from .models import Post,PostLike,PostComment,Profile

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','timestamp','author')

class PostLikeAdmin(admin.ModelAdmin):
    list_display=('id','post_id')

class PostCommentAdmin(admin.ModelAdmin):
    list_display=("id",'user','post_title','comment','parent_title')

    def post_title(self, instance):
        return instance.post.title[:50]+"..."

    post_title.short_description = 'Post Title'
    post_title.admin_order_field = 'post__title'

    def parent_title(self,instance):
        if instance.parent!=None:
            return str(instance.parent.id)+" : "+instance.parent.comment[:50]
        else:
            return "-"

    parent_title.short_description = 'Parent id : Parent Comment'
    #parent_title.admin_order_field = 'postcomment__comment'
    #parent_title.empty_value_display = '-'

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','id','location','birth_date')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(PostLike,PostLikeAdmin)
admin.site.register(PostComment,PostCommentAdmin)
