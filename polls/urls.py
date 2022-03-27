from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('<int:group_id>', views.group_detail, name='group_detail'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('<int:question_id>/submit/', views.submit, name="submit"),

    # Dylan
    path('home', views.groups, name='home'),
    #Cheryl
    path('image_upload', views.image_view, name='image_upload'),

    # home
    path('home', views.groups, name='home'),
    # group details
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
