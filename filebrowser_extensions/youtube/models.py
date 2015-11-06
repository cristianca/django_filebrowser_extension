import os
from django.utils.translation import ugettext_lazy as _
from embed_video.backends import YoutubeBackend
import requests
from filebrowser_extensions.iframes.models import IFrameAbstract
from filebrowser.settings import DIRECTORY, MEDIA_ROOT, MEDIA_URL


YOUTUBE_THUMBNAIL_DIRECTORY = 'youtube_thumbnails'


class Youtube(IFrameAbstract):
    """
    Store information about thing link media lib
    """

    class Meta:
        verbose_name = _('Youtube')
        verbose_name_plural = _('Youtubes')

    def download_youtube_thumbnail(self):
        """
        download youtube thumbnail and save it in uploads folder 'youtube_thumbnails'
        :return: path to to youtube thumbnail
        """

        file_name = '_'.join(self.youtube_thumbnail.split('/')[-2:])
        path = os.path.join(MEDIA_ROOT, DIRECTORY, YOUTUBE_THUMBNAIL_DIRECTORY, file_name)

        r = requests.get(self.youtube_thumbnail, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        return os.path.join(DIRECTORY, YOUTUBE_THUMBNAIL_DIRECTORY, file_name)

    def save(self, *args, **kwargs):
        """
        save object and if thumbnail is not given, get original thumbnail
        from youtube
        """
        if not self.thumbnail:
            self.thumbnail = self.download_youtube_thumbnail()
        super(Youtube, self).save(*args, **kwargs)

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
    def youtube_thumbnail(self):
        """
        return youtube thumbnail
        """
        return self.youtube_backend.thumbnail
