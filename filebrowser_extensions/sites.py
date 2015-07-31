from django.core.files.storage import DefaultStorage
from filebrowser.sites import FileBrowserSite as BaseSite


class FileBrowserSite(BaseSite):
    """
    Extended version of FileBrowser site. Allow to integrate with
    other medias like youtube or thinglink...
    """

    EXTENSION_NAME = 'Files'

    pass


storage = DefaultStorage()
# Default FileBrowser site
site = FileBrowserSite(name='filebrowser', storage=storage)

# Default actions
from filebrowser.actions import (
    flip_horizontal, flip_vertical, rotate_90_clockwise,
    rotate_90_counterclockwise, rotate_180)
site.add_action(flip_horizontal)
site.add_action(flip_vertical)
site.add_action(rotate_90_clockwise)
site.add_action(rotate_90_counterclockwise)
site.add_action(rotate_180)
