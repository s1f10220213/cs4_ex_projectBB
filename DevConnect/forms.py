from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description')
        labels = {'name':'プロジェクト名', 'description':'プロジェクトの説明'}