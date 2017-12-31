from django.contrib import admin

# Register your models here.
from news_app.models import News,Image,NewsImage,Comment
admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(Image)
admin.site.register(Comment)
