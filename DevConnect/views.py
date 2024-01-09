from django.shortcuts import render, redirect
from django.http import Http404
from DevConnect.models import CustomUser, User_Genre, Project, ProjectMembers, Project_detail, Project_recruit_genre, Project_member_genre, Chat

# マイページ
def mypage(request):
    return render(request, "DevConnect/mypage.html")

# プロジェクト作成
def cp(request):
    if request.method == 'POST':
            project = Project(user=request.user)
            project.save()
            
    return redirect(f"http://127.0.0.1:8000/word/cd_genre")

# プロジェクト指定
def project(request):
    return render(request, "DevConnect/project.html")

# プロジェクトページ
def projectin(request, project_name):
    return render(request, "DevConnect/projectin.html", {"project_name": project_name})

# プロジェクト詳細
def projectDetail(request, project_name):
    return render(request, "DevConnect/project_detail.html", {"project_name": project_name})

# プロジェクト検索ページ
def search(request):
    return render(request, "DevConnect/search.html")