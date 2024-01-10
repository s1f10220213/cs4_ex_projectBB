from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.http import Http404
import random
from DevConnect.models import Project, Project_detail, Project_member_genre, Project_recruit_genre, ProjectMembers, User_Genre, Chat, UserManager, CustomUser

# マイページ
def mypage(request):
    return render(request, "DevConnect/mypage.html")

# プロジェクト作成
def cp(request):
    return render(request, "DevConnect/create_project.html")

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
def search(request, id):
    try:
        detail = Project_detail.objects.get(pk=id)
    except detail.DoesNotExist:
        raise Http404("Your page does not exist")
    context = {
        "detail": detail
    }
    return render(request, "DevConnect/search.html", context)