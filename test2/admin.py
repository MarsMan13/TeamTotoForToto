from django.contrib import admin
from .models import Community_post
from .models import Post
from .models import Member_info
from .models import My_unders
from .models import My_roles



admin.site.register(Post)
admin.site.register(Community_post)
admin.site.register(Member_info)
admin.site.register(My_unders)
admin.site.register(My_roles)


# Register your models here.
