from django.utils.translation import ugettext_lazy as _
from filebrowser_extensions.iframes.models import IFrameAbstract


class ThingLink(IFrameAbstract):
    """
    Store information about thing link media lib
    """

    class Meta:
        verbose_name = _('ThingLink')
        verbose_name_plural = _('ThingLinks')

    @property
    def iframe_link(self):
        return self.code.replace('scene', 'card')