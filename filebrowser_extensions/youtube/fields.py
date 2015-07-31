from django import forms
from embed_video.backends import YoutubeBackend, UnknownIdException
from embed_video.fields import EmbedVideoFormField


class YoutubeEmbedFormField(EmbedVideoFormField):
    """
    Extend :class:EmbedVideoFormField to make it work only with youtube
    as in this case we don't want any other links available. We could
    change it in settings by overwrite EMBED_VIDEO_BACKENDS
    but i think it's better to go that way b'coz we might want to use
    embed_video apps to write for example Vimeo extension as well
    """

    def validate(self, url):
        # we need only basic validation from URLField as we are overwriting
        # EmbedVideoFormField validation
        super(forms.URLField, self).validate(url)

        if not url:
            return
        try:
            backend = YoutubeBackend(url)
            backend.get_code()
        except UnknownIdException:
            raise forms.ValidationError(_(u'ID of this video could not be '
                                          u'recognized.'))
        return url
