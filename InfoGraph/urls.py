from django.conf.urls.defaults import *

# your_app = name of your root djang app.
urlpatterns = patterns('InfoGraph.views',
    # First leg of the authentication journey...
    #url(r'^music/$', "index", name="index_player"),
    #url(r'^$', "home"),
    #url(r'^InfoGraph/$',"basic"),
    url(r'^InfoGraph/$',"index"),
    url(r'^InfoGraph/home/$', "main"),
    url(r'^InfoGraph/home/search', "search"),
)
