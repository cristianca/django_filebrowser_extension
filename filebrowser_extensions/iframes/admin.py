from django.contrib import admin

from filebrowser_extensions.admin import FileBrowserAdmin
from filebrowser.settings import ADMIN_THUMBNAIL, VERSIONS
from .models import IFrame as IFrameModel
from .forms import IFrameAdminForm


class IFrameAdmin(FileBrowserAdmin):

    list_display = ('name', 'thumbnail', 'create_at')
    search_fields = ('name',)

    class Media(FileBrowserAdmin.Media):
        js = ('fbextensions/js/FB_IFrameField.js',)

    def get_thumbnail(self, obj):
        """display thumbnail from thinglink"""
        return obj.iframe(
            VERSIONS[ADMIN_THUMBNAIL]['width'],
            VERSIONS[ADMIN_THUMBNAIL]['height']
        )


class IFrame(IFrameAdmin):

    form = IFrameAdminForm


admin.site.register(IFrameModel, IFrame)
