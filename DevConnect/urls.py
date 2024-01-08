from django.urls import path
from . import views

urlpatterns = [
    path('mypage', views.mypage, name='mypage'),
    # path('', views.top, name='my_page'),
    path('project/cp', views.cp, name='cp'), # CreateProject新規プロジェクト作成
    path('project', views.project, name='project'), # プロジェクトルーム選択
    path('project/<str:project_name>', views.projectin, name='projectin'), # プロジェクトルーム
]