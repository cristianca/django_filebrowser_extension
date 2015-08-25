from django.utils.translation import ugettext_lazy as _
from embed_video.backends import YoutubeBackend
from filebrowser_extensions.iframes.models import IFrameAbstract


class Youtube(IFrameAbstract):
    """
    Store information about thing link media lib
    """

    class Meta:
        verbose_name = _('Youtube')
        verbose_name_plural = _('Youtubes')

    @property
    def youtube_backend(self):
        """
        :return: youtube backend class from embed_video (very very nice lib)
        """
        if not hasattr(self, '_youtube_backend'):
            self._youtube_backend = YoutubeBackend(self.code)
        return self._youtube_backend

    @property
    def iframe_link(self):
        """
        transform youtube link to youtube embed link
        :return: youtube embed link
        """
        return self.youtube_backend.url

    @property
    def thumbnail(self):
        """
        return youtube thumbnail
        """
        return self.youtube_backend.thumbnail


