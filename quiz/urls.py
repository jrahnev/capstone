from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('start', views.start, name='start'),
    path('display', views.display, name='display'),
    path('newquestion/<str:answer>', views.newquestion, name='newquestion'),
    path('end', views.end, name='end')
]