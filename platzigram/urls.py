from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as posts_views

#media imagen
from django.conf.urls.static import static
from django.conf import settings
from users import views as users_views

from django.views.static import serve

urlpatterns = [
    url('media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url('users/login', users_views.login_view, name='login'),
    url('posts/new', posts_views.create_post, name='create'),
    url('admin/', admin.site.urls),
    url('users/logout', users_views.logout_view, name='logout'),
    url('users/signup', users_views.signup, name='signup'),
    url('users/me/profile', users_views.update_profile, name='update_profile'),
    url('(?P<username>.*)$/', users_views.detail, name='detail'),
    url('', posts_views.list_posts, name='feed')
]
