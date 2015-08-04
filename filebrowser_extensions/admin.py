from django.contrib import admin
from django.contrib.admin.options import IS_POPUP_VAR
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from filebrowser.settings import ADMIN_THUMBNAIL, VERSIONS
from filebrowser_extensions.apps import FilebrowserExtension


class FileBrowserAdmin(admin.ModelAdmin):
    """
    Base admin for filebrowser extensions
    """

    class Media:
        css = {
            'all': ('fbextensions/css/fbe.css',)
        }

    def changelist_view(self, request, extra_context=None):
        """
        Make sure we pass popup var to admin. We do it this way
        to be ok with a way of how filebrowser put popup var from get
        """

        if extra_context is None:
            extra_context = {}

        pop = request.GET.get(IS_POPUP_VAR, None)
        self._pop = pop
        if pop:
            extra_context.update({'query': {'pop': self._pop}})

        extra_context.update(
            {'filebrowser_site':
                 {'extensions': FilebrowserExtension.extensions()}}
        )

        return super(FileBrowserAdmin, self).changelist_view(
            request, extra_context)

    def get_list_display(self, request):
        """
        if popup we need to add additional field to display select button
        """
        ld = list(self.list_display)
        if self._pop:
            ld.insert(0, 'select_item')
        return ld

    def get_list_display_links(self, request, list_display):
        """
        Make sure that if it's popup select link is not the first one
        """
        if self.list_display_links or self.list_display_links is None\
                or not list_display:
            return self.list_display_links
        else:
            # Use only the first item in list_display as link
            if self._pop:
                return list(list_display)[1:2]
            else:
                return list(list_display)[:1]

    def get_thumbnail(self, obj):
        raise NotImplementedError

    def select_item(self, obj):
        """
        allow to select item from popup
        """
        opts = self.model._meta
        app_label = opts.app_label

        context = {
            'content_type': '%s.%s' % (app_label, opts.model_name),
            'object_id': obj.pk,
            'link': obj.iframe_link,
            'width': VERSIONS[ADMIN_THUMBNAIL]['width'],
            'heigth': VERSIONS[ADMIN_THUMBNAIL]['height'],
        }
        return render_to_string([
            '%s/%s/select_item.html' % (app_label, opts.model_name),
            '%s/select_item.html' % app_label,
            'filebrowser/select_item.html'
        ], context)

    select_item.allow_tags = True
    select_item.short_description = _('Select')

    def thumbnail(self, obj):
        return self.get_thumbnail(obj)

    thumbnail.allow_tags = True
    thumbnail.short_description = _('Preview')
