from django.core.urlresolvers import reverse
from filebrowser_extensions.apps import FilebrowserExtension


class ThinglinkFilebrowserExtension(FilebrowserExtension):
    """
    App definition for youtube
    """

    name = 'filebrowser_extensions.thinglink'
    verbose_name = 'Thinglink'

    @classmethod
    def browse_url(cls):
        return reverse('admin:thinglink_thinglink_changelist')