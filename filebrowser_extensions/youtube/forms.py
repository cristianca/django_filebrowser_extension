from django import forms
from django.utils.translation import ugettext_lazy as _

from filebrowser_extensions.youtube.fields import YoutubeEmbedFormField

from .models import Youtube
from .youtube_api import YoutubeApi


class YoutubeAdminForm(forms.ModelForm):
    """
    Form used in admin to make sure that link to video is correct youtube
    """

    code = YoutubeEmbedFormField()

    class Meta:
        model = Youtube
        fields = ('name', 'code', 'thumbnail')


class YoutubeForm(forms.Form):
    """
    Form used to search data over the youtube.
    """

    q = forms.CharField(label=_('YouTube Query'))

    def __init__(self, *args, **kwargs):
        self.page_token = kwargs.pop('page_token')
        super(YoutubeForm, self).__init__(*args, **kwargs)

    def search(self):
        """
        make a search over youtube based on query in 'q' field.
        Search will start only if form is valid.

        :return: tuple of items in response, nextPageToken and prevPageToken
        if exists
        """
        assert self.is_valid()

        youtube_api = YoutubeApi()

        if self.page_token:
            params = {'pageToken': self.page_token}
        else:
            params = None

        response = youtube_api.search_videos(
            query=self.cleaned_data['q'], params=params)
        return (
            response.get('items', []),
            response.get('nextPageToken', None),
            response.get('prevPageToken', None)
        )


class MoveToYoutubeForm(forms.Form):
    """
    Form used to move information about movie from youtube to our library
    """
    name = forms.CharField(label=_('Name'), widget=forms.HiddenInput)
    video_id = forms.CharField(label=_('Video ID'), widget=forms.HiddenInput)

    def save(self):
        youtube = Youtube(
            name=self.cleaned_data['name'],
            code='https://youtu.be/%s' % self.cleaned_data['video_id']
        )
        youtube.save()
