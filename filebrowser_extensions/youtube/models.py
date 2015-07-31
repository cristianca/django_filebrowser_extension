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
    def iframe_link(self):
        """
        transform youtube link to youtube embed link
        :return: youtube embed link
        """
        backend = YoutubeBackend(self.code)
        return backend.url
