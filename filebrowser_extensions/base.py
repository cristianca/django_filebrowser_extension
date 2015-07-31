from django.db.models.loading import get_model
from filebrowser.settings import ADMIN_THUMBNAIL, VERSIONS
from .exceptions import FBExtensionObjectException

CORECT_FORMAT_EXCEPTION = 'Correct value format is: app_label.model_name:pk'


class FBExtensionObject(object):
    """
    Helper class to manage extension objects. Like youtube video, thinglink
    and others...
    """

    def __init__(self, value, version_suffix=ADMIN_THUMBNAIL):
        """
        Initialize Media for filebrowser.
        :param value: string with format 'app_label.model_name:pk'
        :param version_suffix: string with information about version to display

        """

        assert isinstance(value, str)
        assert version_suffix in VERSIONS.keys()

        self.value = value

        try:
            model_representation, self.object_id = value.split(':')
        except ValueError:
            raise FBExtensionObjectException(CORECT_FORMAT_EXCEPTION)

        if not all((model_representation, self.object_id)):
            raise FBExtensionObjectException(CORECT_FORMAT_EXCEPTION)

        try:
            self.app_label, self.model_name = model_representation.split('.')
        except ValueError:
            raise FBExtensionObjectException(CORECT_FORMAT_EXCEPTION)
        self.version_suffix = version_suffix

    def __len__(self):
        return len(self.value)

    @property
    def content_object(self):
        """
        return extended object related to fb extension
        """
        model = get_model(self.app_label, self.model_name)
        try:
            return model.objects.get(pk=self.object_id)
        except model.DoesNotExist:
            return None

    @property
    def exists(self):
        """
        :return: True if related object exists
        """
        return bool(self.content_object)

    @property
    def height(self):
        return VERSIONS[self.version_suffix]['height']

    @property
    def path(self):
        """
        It's called path just to be ok with naming in filebrowser
        :return: model_representation and id
        """
        return self.value

    @property
    def iframe(self):
        return self.content_object.iframe(width=self.width, height=self.height)

    @property
    def filetype(self):
        """
        Filetype name is used to be ok with filebrowser naming.
        :return: type of the conent
        """
        if hasattr(self.content_object, 'iframe'):
            return 'IFrame'

    @property
    def width(self):
        return VERSIONS[self.version_suffix]['width']

    def version_generate(self, version_suffix):
        """Generate Version for media"""
        return FBExtensionObject(self.value, version_suffix=version_suffix)
