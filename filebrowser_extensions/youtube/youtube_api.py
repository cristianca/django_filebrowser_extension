import requests
from .consts import API_KEY, RESULTS_PER_PAGE


class YoutubeApi(object):
    urls = {
        'search': 'https://www.googleapis.com/youtube/v3/search',
    }
    default_params = {}

    def __init__(self, api_key=API_KEY):

        assert isinstance(API_KEY, str)

        self.key = api_key
        self.default_params = {
            'key': self.key,
            'part': 'snippet',
        }

    def get_params(self, *args):
        """ Merge custom params with default params """
        result = {}
        for dictionary in args:
            if isinstance(dictionary, dict):
                result.update(dictionary)
        return result

    def search(self, query, max_results=RESULTS_PER_PAGE, params=None):
        """
        search over youtube using given query and max_results per page,
        possible to put additional params
        """

        assert isinstance(query, str)
        assert isinstance(max_results, int)

        params = self.get_params(self.default_params, {
            'q': query,
            'maxResults': max_results
        }, params)
        result = requests.get(self.urls['search'], params=params)
        return result.json()

    def search_videos(self, query, max_results=RESULTS_PER_PAGE, params=None):
        """
        use exactly the same what we have in search except we search here
        only type=video
        """

        params = self.get_params({
            'type': 'video'
        }, params)
        return self.search(query, max_results=max_results, params=params)
