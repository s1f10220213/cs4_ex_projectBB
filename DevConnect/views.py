from django.shortcuts import render

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