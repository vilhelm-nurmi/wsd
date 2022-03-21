
from django.urls import path,include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin', admin.site.urls, name = 'admin'),
    path('', views.homepage, name = 'home'),
    path('toplist/', views.toplist, name = 'toplist'),
    path('complaints/', views.complaints, name = 'complaints'),
    path('search/',include('search.urls'), name = 'search, search_result'),
    path('games/',include('games.urls'),name = 'games'),
    path('',include('accounts.urls'),name = 'signup, login, logout'),
    path('',include('shop.urls'),name = 'shop, error, success, cancel'),
    path('api/v1/', include('social_django.urls'), name='social'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
