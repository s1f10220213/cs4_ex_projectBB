from django.urls import path
from . import views

urlpatterns = [
    # path('', views.mypage, name='mypage'),
    # path('', views.top, name='my_page'),
    path('project', views.project, name='project'),
    path('project/<str:project_name>', views.projectin, name='projectin'),
]