from django.contrib import admin
from filebrowser_extensions.iframes.admin import IFrameAdmin
from .models import ThingLink


class ThingLinkAdmin(IFrameAdmin):
    pass


admin.site.register(ThingLink, ThingLinkAdmin)
