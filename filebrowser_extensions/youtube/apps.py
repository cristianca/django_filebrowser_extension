from django.core.urlresolvers import reverse
from filebrowser_extensions.apps import FilebrowserExtension


class YoutubeFilebrowserExtension(FilebrowserExtension):
    """
    App definition for youtube
    """

    name = 'filebrowser_extensions.youtube'
    verbose_name = 'Youtube'

    @classmethod
    def browse_url(cls):
        return reverse('admin:youtube_youtube_changelist')