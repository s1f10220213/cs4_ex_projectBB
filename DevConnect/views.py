from django.shortcuts import render, redirect
from django.http import Http404
from django.utils import timezone
from .forms import ProjectForm
from DevConnect.models import Project, ProjectMembers, User_Genre, Chat, CustomUser

# マイページ
def mypage(request):
    return render(request, "DevConnect/mypage.html")

# プロジェクト作成
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
    try:
        detail = Project.objects.get(name=project_name)
        members = ProjectMembers.objects.get(project=detail[0].id)
        genres = Project.objects.get(project=detail[0].id)

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
        gen = ""

        if 'programmer' in request.POST:
            gen += "programmer_"
        if 'designer' in request.POST:
            gen += "designer_"
        if 'production' in request.POST:
            gen += "production_"
        if 'sound' in request.POST:
            gen += "sound"
        
        return redirect("DevConnect/search_result.html", genres=gen)
    return render(request, "DevConnect/search.html")

# 検索結果ページ
def search_result(request, genres):
    projects = []
    genre_parts = genres.split('_')
    for i in genre_parts:
        ids = ProjectGenre.objects.filter(genre=i)
        for j in ids:
            pro = Project_detail.objects.filter(id=j)
            if pro[0] in details:
                continue
            else:
                projects.append(pro[0])
    context = {
        "projects": projects,
    }
    return render(request, "DevConnect/search_result.html", context)