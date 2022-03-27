from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'polls'
urlpatterns = [
    # group details
    path('group/<int:group_id>', views.group_detail, name='group_detail'),
    # path('<int:question_id>/', views.detail, name='detail'),

    # Dylan
    path('home', views.groups, name='home'),
    #Cheryl
    # path('image_upload', views.image_view, name='image_upload'),

    # home
    path('home', views.groups, name='home'),

    #photo gallery
    path('group/image_gallery/<int:group_id>', views.image_gallery, name = 'image_gallery'),

    path('group/submission', views.image_view, name='image_upload'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        # urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 

