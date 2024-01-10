from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, user_id, user_name, password=None):
        if not user_id:
            raise ValueError('ユーザーIDが必要です')
        if not user_name:
            raise ValueError('ニックネームが必要です')

        user = self.model(
            user_id=user_id,
            user_name=user_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_name, password):
        user = self.create_user(
            user_id=user_id, 
            user_name=user_name,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=25, unique=True)
    user_name = models.CharField(max_length=25, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name

class User_Genre(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

### Project #####################################################
    
class Project(models.Model):
    user = models.ManyToManyField(CustomUser, through='ProjectMembers')

class ProjectMembers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)

class Project_detail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    explain = models.TextField()
    leader = models.ForeignKey(CustomUser, related_name='project_leadership', on_delete=models.SET_NULL, null=True)

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