from django.contrib import admin
from .models import Community_post
from .models import Post
from .models import Member_info


admin.site.register(Post)
admin.site.register(Community_post)
admin.site.register(Member_info)

# Register your models here.
