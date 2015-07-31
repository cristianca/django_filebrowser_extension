from functools import update_wrapper
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from filebrowser_extensions.iframes.admin import IFrameAdmin
from .forms import YoutubeForm, MoveToYoutubeForm, YoutubeAdminForm

from .models import Youtube


class YoutubeAdmin(IFrameAdmin):
    """
    Give additional options for user to have search over youtube enabled
    """

    form = YoutubeAdminForm

    def changelist_view(self, request, extra_context=None, page_token=None):
        """
        Extend normal admin changelist view to add youtube video searchs.
        We search only if youtube form is valid. (Youtube form requires
        query phrase to be available in get)

        We also might push page_token to youtube. We can not put page_token
        in GET b'coz django admin check params and will make redirect if
        GET param is not on the list. It's hard to overwrite that behaviour.
        So we put additional view for that to pass token in url path
        """
        youtube_form = YoutubeForm(request.GET, page_token=page_token)

        if youtube_form.is_valid():

            def move_to_library_form(youtube_result):
                form = MoveToYoutubeForm(initial={
                    'name': youtube_result['snippet']['title'],
                    'video_id': youtube_result['id']['videoId']
                })
                return {'result': youtube_result,
                        'form': form}

            youtube_results, next_token, prev_token = youtube_form.search()
            extra_context = {
                'youtube_results': list(
                    map(move_to_library_form, youtube_results)),
                'next_page_token': next_token,
                'prev_page_token': prev_token,
                'search_query': youtube_form.cleaned_data['q']
            }

        return super(YoutubeAdmin, self).changelist_view(
            request, extra_context)

    def move_to_library(self, request):
        """
        view to move youtube videos from youtube search results to extension
        library and save in
        :class:`filebrwoser_extensions.youtube.models.Youtube`

        after that view should return 302 redirect to youtube changelist
        as well
        """
        form = MoveToYoutubeForm(request.POST)
        if form.is_valid():
            form.save()

        redirect_url = reverse('admin:youtube_youtube_changelist')
        redirect_url += '?q=' + request.GET['q']
        is_popup = request.GET.get('_popup')
        if is_popup:
            redirect_url += '&_popup=1'

        return HttpResponseRedirect(redirect_url)

    def get_urls(self):
        """
        Overwrite default urls to add 2 custom views.
        """
        urls = super(YoutubeAdmin, self).get_urls()

        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        urlpatterns = [
            url(r'^move_to_library/$',
                wrap(self.move_to_library), name='youtube_move_to_library'),
            url(r'^token/(?P<page_token>[-\w]+)/$',
                wrap(self.changelist_view), name='youtube_changelist_token'),
            ]

        return urlpatterns + urls


admin.site.register(Youtube, YoutubeAdmin)

