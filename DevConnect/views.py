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
    if request.method == 'POST':
        project = Project.objects.get(name=project_name)
        chat = Chat(project=project, user=CustomUser.objects.get(pk=request.user.id), content=request.POST["content"])
        chat.save()
        return redirect(projectin, project.name)
    else:
        project = Project.objects.get(name=project_name)
        menbers = project.members.all()
        context = {
            "project":Project.objects.filter(members=CustomUser.objects.get(pk=request.user.id)),
            "chat" : Chat.objects.filter(project=project.id),
            "member":menbers,
            "project_name": project_name
        }
        return render(request, "DevConnect/projectin.html", context)

# チャット
def chat(request, project_name):
    if request.method == 'POST':
        project = Project.objects.get(name=f"{project_name}")
        chat = Chat(project=project.id, user=request.user.id, content=request.POST["content"])
        chat.save()
    return redirect(projectin, project_name)

# プロジェクト詳細
def projectDetail(request, id):
    try:
        detail = Project_detail.objects.get(pk=id)
        members = ProjectMembers.objects.get(project=detail.project)
        genres = Project_recruit_genre.objects.get(project=detail.project)

    except detail.DoesNotExist:
        raise Http404("Your page does not exist")
    context = {
        "detail": detail,
        "members": members,
        "genres": genres
    }
    return render(request, "DevConnect/project_detail.html", context)

# プロジェクト検索ページ
def search(request):
    if request.method == "POST":
        newProject = Project_detail(title=request.POST["title"], body=request.POST["body"], user_name=request.POST["username"], user_pass=request.POST["userpass"])

        newProject.save()
        context = {
            "mypage": mypage
        }
        return render(request, "hobitalk/detail.html", context)
    return render(request, "DevConnect/search.html", context)