# coding: utf-8

# DJANGO IMPORTS
from django.template import Library, Node, \
    VariableDoesNotExist, TemplateSyntaxError
from django.conf import settings
from django.core.files import File


# FILEBROWSER IMPORTS
from filebrowser.settings import VERSIONS, PLACEHOLDER,\
    SHOW_PLACEHOLDER, FORCE_PLACEHOLDER
from filebrowser.base import FileObject
from filebrowser.sites import get_default_site
from filebrowser.templatetags.fb_versions import \
    VersionObjectNode as BaseVersionObjectNode

from filebrowser_extensions.base import FBExtensionObject


register = Library()


class VersionNode(Node):
    def __init__(self, src, suffix):
        self.src = src
        self.suffix = suffix

    def render(self, context):
        try:
            version_suffix = self.suffix.resolve(context)
            source = self.src.resolve(context)
        except VariableDoesNotExist:
            return ""
        if version_suffix not in VERSIONS:
            return ""  # FIXME: should this throw an error?
        if isinstance(source, FileObject):
            source = source.path
        elif isinstance(source, File):
            source = source.name
        else:  # string
            source = source
        site = context.get('filebrowser_site', get_default_site())
        if FORCE_PLACEHOLDER or (SHOW_PLACEHOLDER and not site.storage.isfile(source)):
            source = PLACEHOLDER
        fileobject = FileObject(source, site=site)
        try:
            version = fileobject.version_generate(version_suffix)
            return version.url
        except Exception as e:
            if settings.TEMPLATE_DEBUG:
                raise e
        return ""


def fbe_version(parser, token):
    """
    Displaying a version of an existing Image according to the predefined VERSIONS settings (see filebrowser settings).
    {% version fileobject version_suffix %}

    Use {% version fileobject 'medium' %} in order to
    display the medium-size version of an image.
    version_suffix can be a string or a variable. if version_suffix is a string, use quotes.
    """

    bits = token.split_contents()
    if len(bits) != 3:
        raise TemplateSyntaxError("'version' tag takes 4 arguments")
    return VersionNode(parser.compile_filter(bits[1]), parser.compile_filter(bits[2]))


class VersionObjectNode(BaseVersionObjectNode):
    """
    Extend default filebrowser VersionObjectNode to make sure
    it might support other media files
    """

    def render(self, context):
        try:
            version_suffix = self.suffix.resolve(context)
            source = self.src.resolve(context)
        except VariableDoesNotExist:
            return None
        if version_suffix not in VERSIONS:
            return ""  # FIXME: should this throw an error?
        if isinstance(source, FBExtensionObject):
            fileobject = source
        else:
            if isinstance(source, FileObject):
                source = source.path
            elif isinstance(source, File):
                source = source.name
            else:  # string
                source = source
            site = context.get('filebrowser_site', get_default_site())
            if FORCE_PLACEHOLDER or (SHOW_PLACEHOLDER and not site.storage.isfile(source)):
                source = PLACEHOLDER
            fileobject = FileObject(source, site=site)
        try:
            version = fileobject.version_generate(version_suffix)
            context[self.var_name] = version
        except Exception as e:
            if settings.TEMPLATE_DEBUG:
                raise e
            context[self.var_name] = ""
        return ""


def fbe_version_object(parser, token):
    """
    Overwrite :func:`filebrowser.templates.fb_versions` to make sure
    we can use extend node
    """

    bits = token.split_contents()
    if len(bits) != 5:
        raise TemplateSyntaxError("'version_object' tag takes 4 arguments")
    if bits[3] != 'as':
        raise TemplateSyntaxError("second argument to 'version_object' tag must be 'as'")
    return VersionObjectNode(parser.compile_filter(bits[1]), parser.compile_filter(bits[2]), bits[4])


register.tag(fbe_version)
register.tag(fbe_version_object)
