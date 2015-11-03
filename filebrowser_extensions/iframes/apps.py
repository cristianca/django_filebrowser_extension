from django.core.urlresolvers import reverse
from filebrowser_extensions.apps import FilebrowserExtension


class IFrameFilebrowserExtension(FilebrowserExtension):
    """
    App definition for Iframe
    """

    name = 'filebrowser_extensions.iframes'
    verbose_name = 'IFrame'

    @classmethod
    def browse_url(cls):
        return reverse('admin:iframes_iframe_changelist')