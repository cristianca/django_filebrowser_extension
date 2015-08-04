# django_filebrwoser_extension #

Extension for [django-filebrowser](https://github.com/sehmaschine/django-filebrowser/ "django-filebrowser") that allows to 
use filebrowser not only for files but also for medias from 3'rd part services like:

* [youtube](https://youtube.com/ "youtube")
* [thinglink](https://www.thinglink.com/ "thinglink")
* More to come


# Install #

pip install -e git+git@github.com:tomaszroszko/django_filebrowser_extension.git#egg=django_filebrowser_extension-master

# Setup #

In your settings.py


```python
INSTALLED_APPS = (

    'grappelli',
    'filebrowser_extensions',
    'filebrowser_extensions.thinglink',
    'filebrowser_extensions.youtube',
    'filebrowser',
    'django.contrib.admin',

```

In urls.py


```python
from django.conf.urls import include, patterns
from django.contrib import admin
from filebrowser_extensions.sites import site


urlpatterns = patterns('',
   (r'^admin/filebrowser/', include(site.urls)),
   (r'^grappelli/', include('grappelli.urls')),
   (r'^admin/', include(admin.site.urls)),
)
```

Some screen shots:

![File Browser Youtube Integration](https://raw.githubusercontent.com/tomaszroszko/django_filebrowser_extension/master/docs/youtube.png)
![File Browser Youtube Integration](https://raw.githubusercontent.com/tomaszroszko/django_filebrowser_extension/master/docs/youtube2.png)