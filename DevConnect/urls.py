from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypage, name='mypage'), # 後でリンクをmypageにすること
    path('mypage', views.mypage, name='mypage'),
    path('project/cp', views.cp, name='cp'), # CreateProject新規プロジェクト作成
    path('project', views.project, name='project'), # プロジェクトルーム選択
    path('project/<str:project_name>', views.projectin, name='projectin'), # プロジェクトルーム
    path('chat/<str:project_name>', views.chat, name='chat'), # チャット内容保存
    path('projectDetail/<str:project_name>', views.projectDetail, name='projectDetail'), # プロジェクト詳細
    path('search', views.search, name='search'), # プロジェクト検索
]