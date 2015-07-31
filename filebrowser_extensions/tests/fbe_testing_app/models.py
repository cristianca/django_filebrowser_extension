from django.db import models
from filebrowser_extensions.fields import FileBrowseField
from filebrowser_extensions.iframes.models import IFrameAbstract


class FBETestModel(models.Model):
    """model used for FBE tests"""

    title = models.CharField(max_length=255)
    file_example = FileBrowseField(max_length=500)

    def __str__(self):
        return self.title


class TestExtension(IFrameAbstract):
    pass