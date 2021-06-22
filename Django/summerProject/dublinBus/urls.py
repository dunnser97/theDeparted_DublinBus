from django.urls import path

from . import views

urlpatterns = [
    # ex: /dublinBus
    path('', views.index, name='index'),
    # ex: /dublinBus/scrapeCW
    path('scrapeCW', views.scrapeCW, name='scrapeCW'),
    #ex: /dublinBus/2/
    path('<int:entry_id>/', views.detail, name='detail'),
]