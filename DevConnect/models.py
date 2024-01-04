from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=25, unique=True)
    user_name = models.TextField()
    user_password = models.CharField(max_length=25)

class User_Genre(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

### Project #####################################################

class ProjectMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Project_detail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    explain = models.TextField()
    leader = models.ForeignKey(User, related_name='project_leadership', on_delete=models.SET_NULL, null=True)

class Project_genre(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

### Chat ########################################################

class Chat(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)