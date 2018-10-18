from django.urls import path
from . import views

urlpatterns = [
    #ex: /getnewsurl/
    path('', views.index, name='index'),

    # view news, ex: /getnewsurl/5
    path('<int:news_id>/', views.viewNews, name='news-details'),

    # view news stance, ex: getnewsurl/5/stance 
    path('<int:news_id>/stance', views.viewNewsStance, name='news-stance'),
]