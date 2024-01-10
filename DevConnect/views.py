from django.shortcuts import render, redirect
from django.http import Http404
from django.utils import timezone
from .forms import ProjectForm
from DevConnect.models import CustomUser, Genre, User_Genre, Project, ProjectMembers, Chat
from django.contrib.auth.decorators import login_required

# マイページ
def mypage(request):
    return render(request, "DevConnect/mypage.html")

# プロジェクト作成
@login_required
def cp(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = Project(name=form.cleaned_data['name'] ,description=form.cleaned_data['description'] ,leader=CustomUser.objects.get(pk=request.user.id))
            project.save()
            project.add_leader_to_members()
            return redirect(projectin, project.name)
    else:
        form = ProjectForm()
        context = {'form': form}
        return render(request, "DevConnect/create_project.html", context)

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