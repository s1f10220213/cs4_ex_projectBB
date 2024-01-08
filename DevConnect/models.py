from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=25, unique=True)
    user_name = models.TextField()
    user_password = models.CharField(max_length=25)

class User_Genre(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

### Project #####################################################
    
class Project(models.Model):
    user = models.ManyToManyField(User, through='ProjectMembers')

class ProjectMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Project_detail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    explain = models.TextField()
    leader = models.ForeignKey(User, related_name='project_leadership', on_delete=models.SET_NULL, null=True)

class Project_recruit_genre(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

class Project_member_genre(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

### Chat ########################################################

class Chat(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

### Genre #######################################################

# class Genre(models.Model):
#     name = models.CharField(max_length=100)