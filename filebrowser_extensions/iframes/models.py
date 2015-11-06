import os
from django.db import models
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from bs4 import BeautifulSoup
from embed_video.backends import VimeoBackend
from filebrowser.fields import FileBrowseField
from filebrowser.settings import MEDIA_ROOT, DIRECTORY
import requests
from .consts import IFRAMES_DETECTION, IFRAME_VIMEO, IFRAME_DAILYMOTION


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
        iframe = self.iframe_soup
        iframe['width'] = width
        iframe['height'] = height
        return mark_safe(iframe.prettify())

    @property
    def iframe_soup(self):
        """
        :return: bs4 iframe object
        """
        if not hasattr(self, '__iframe_soup__'):
            soup = BeautifulSoup(self.code)
            self.__iframe_soup__ = soup.find('iframe')
        return self.__iframe_soup__

    @property
    def iframe_src(self):
        return self.iframe_soup['src']

    @property
    def iframe_type(self):
        for iframe_type, iframe_url in IFRAMES_DETECTION.items():
            if iframe_url in self.iframe_src:
                return iframe_type
        return None

    def download_thumbnail(self, thumbnail, file_name, directory):
        # TODO: this solution is temporary, need to rewrite that
        path = os.path.join(MEDIA_ROOT, DIRECTORY, directory, file_name)
        r = requests.get(thumbnail, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        return os.path.join(DIRECTORY, directory, file_name)

    def save(self, *args, **kwargs):
        """
        Save and check if we can recognize what type of iframe it is (from what service)
        so we can for example add thumbnail automaticly
        """

        # TODO: make it nice easy to extend and so on...
        if not self.thumbnail:
            t = self.iframe_type
            if t == IFRAME_VIMEO:
                vimeo = VimeoBackend(self.code)
                thumbnail = vimeo.get_thumbnail_url()
                file_name = thumbnail.split('/')[-1]
                self.thumbnail = self.download_thumbnail(thumbnail, file_name, 'vimeo_thumbnails')
            elif t == IFRAME_DAILYMOTION:
                thumbnail = self.iframe_src.replace('embed', 'thumbnail')
                file_name = thumbnail.split('/')[-1] + '.jpg'
                self.thumbnail = self.download_thumbnail(thumbnail, file_name, 'dailymontion_thumbnails')


        super(IFrame, self).save(*args, **kwargs)