from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.groups, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('<int:question_id>/submit/', views.submit, name="submit"),

    # path(r'^submit/$', views.submit),

    # home
    path('home', views.groups, name='home'),
    # group details
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
]