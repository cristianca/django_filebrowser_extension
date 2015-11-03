from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from bs4 import BeautifulSoup
from filebrowser.fields import FileBrowseField


class IFrameAbstract(models.Model):
    """
    Store information about thing link media lib
    """

    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    name = models.CharField(_('Name'), max_length=255)
    thumbnail = FileBrowseField(
        _('Thumbnail'),
        null=True,
        blank=True,
        help_text=_('Upload thumbnail of your video / iframe / sliedshow'),
        max_length=255
    )

    code = models.CharField(
        _('Code'), max_length=1000,
        help_text=_('Copy paste link to iframe here'),
        unique=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def iframe(self, width, height):
        return render_to_string(
            'filebrowser/iframe.html',
            {
                'link': self.iframe_link,
                'width': width,
                'height': height
            }
        )

    @property
    def iframe_link(self):
        return self.code


class IFrame(IFrameAbstract):
    """
    Support for adding iframe code to library.
    Generally in :param:`code` we store full iframe code
    """

    def iframe(self, width, height):
        """
        Normally to display iframe code we have to only display what we have
        on :param:`code` but b'coz we can get different width and height, we need
        to edit that
        """
        soup = BeautifulSoup(self.code)
        iframe = soup.find('iframe')
        iframe['width'] = width
        iframe['height'] = height
        return mark_safe(iframe.prettify())
