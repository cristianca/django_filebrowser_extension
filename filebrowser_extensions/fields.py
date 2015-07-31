import os
from django.core import urlresolvers
from django.db.models import CharField
from django.template.loader import render_to_string

from filebrowser.base import FileObject
from filebrowser.fields import FileBrowseField as BaseFileBrowseField
from filebrowser.fields import FileBrowseFormField as BaseFileBrowserFormField
from filebrowser.fields import FileBrowseWidget as BaseFileBrowseWidget
from filebrowser.settings import ADMIN_THUMBNAIL

from .base import FBExtensionObject
from .utils import is_extend_value


class FileBrowseWidget(BaseFileBrowseWidget):
    """
    Extend default filebrowse widget to allow other medias like yt or
    thingling to be served
    """
    def render(self, name, value, attrs=None):
        url = urlresolvers.reverse(self.site.name + ":fb_browse")
        if value is None:
            value = ""
        if value != "" and not isinstance(
                value, (FileObject, FBExtensionObject)):

            if is_extend_value(value):
                value = FBExtensionObject(value)
            else:
                value = FileObject(value, site=self.site)

        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        final_attrs['url'] = url
        final_attrs['directory'] = self.directory
        final_attrs['extensions'] = self.extensions
        final_attrs['format'] = self.format
        final_attrs['ADMIN_THUMBNAIL'] = ADMIN_THUMBNAIL
        filebrowser_site = self.site

        if value != "":
            try:
                final_attrs['directory'] = os.path.split(value.original.path_relative_directory)[0]
            except:
                pass
        return render_to_string("filebrowser/custom_field.html", locals())


class FileBrowseFormField(BaseFileBrowserFormField):
    """
    Extend default filebrowse form field to allow other medias like yt or
    thinglink to be served
    """
    pass


class FileBrowseField(BaseFileBrowseField):
    """
    Extend default filebrowse fields for to allow other medias like yt
    or thinglink
    """

    def to_python(self, value):
        """
        All custom extension has special way of saying witch is
        app_name.model:object_id. If we detected that that's the case
        we use FBExtensionObject not FileObject
        """

        if not value or isinstance(value, (FileObject, FBExtensionObject)):
            return value

        if is_extend_value(value):
            return FBExtensionObject(value)
        else:
            return FileObject(value, site=self.site)

    def formfield(self, **kwargs):
        attrs = {}
        attrs["filebrowser_site"] = self.site
        attrs["directory"] = self.directory
        attrs["extensions"] = self.extensions
        attrs["format"] = self.format
        defaults = {
            'form_class': FileBrowseFormField,
            'widget': FileBrowseWidget(attrs=attrs),
            'filebrowser_site': self.site,
            'directory': self.directory,
            'extensions': self.extensions,
            'format': self.format
        }
        return super(CharField, self).formfield(**defaults)
