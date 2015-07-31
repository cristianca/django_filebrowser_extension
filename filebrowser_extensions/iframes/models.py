from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


class IFrameAbstract(models.Model):
    """
    Store information about thing link media lib
    """

    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    name = models.CharField(_('Name'), max_length=255)

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