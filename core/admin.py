from django.contrib import admin

from .models import User, Item, Interest, Comment, Item_Detail_View


admin.site.register(User)
admin.site.register(Item)
admin.site.register(Interest)
admin.site.register(Comment)
admin.site.register(Item_Detail_View)