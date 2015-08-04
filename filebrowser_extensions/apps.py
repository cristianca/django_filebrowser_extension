from django.apps import AppConfig


class FilebrowserExtension(AppConfig):
    """
    Base App for filebrowser extensions
    """

    name = 'filebrowser_extensions'
    verbose_name = 'Filebrowser Extensions'

    available_extensions = []

    def ready(self):
        """
        If app config is based on this class we add to available_extensions
        so we can easily track all available applications
        """
        super(FilebrowserExtension, self).ready()

        if not (self.__class__ == FilebrowserExtension):
            self.__class__.available_extensions.append(self.__class__)

    @classmethod
    def extensions(cls):
        return list(map(
            lambda x: {'name': x.verbose_name, 'browse_url': x.browse_url},
            cls.available_extensions
        ))

    @classmethod
    def browse_url(cls):
        """url to view presenting media from extension"""
        raise NotImplementedError