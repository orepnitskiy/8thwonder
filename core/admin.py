from django.contrib import admin
from core.models import TwitterTokens, InstagramTokens,Group
# Register your models here.
admin.site.register(TwitterTokens)
admin.site.register(InstagramTokens)
admin.site.register(Group)