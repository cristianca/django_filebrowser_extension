from django.conf import settings


API_KEY = getattr(settings, 'YOUTUBE_API_KEY', None)
RESULTS_PER_PAGE = getattr(settings, 'YOUTUBE_RESULTS_PER_PAGE', 20)
