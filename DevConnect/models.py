from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
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
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        return self.user_name


### Genre #######################################################

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:  # pk (primary key) が None の場合、新しいオブジェクトが作成されていることを示します
            # 初期化時に実行したい処理をここに書けます
            # 例: name フィールドにデフォルト値をセットする
            self.name = "デフォルトの名前"
            
        super().save(*args, **kwargs)  # 親クラスの `save()` メソッドを呼び出す

class User_Genre(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

### Project #####################################################
    
class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    leader = models.ForeignKey(CustomUser, related_name='project_leadership', on_delete=models.SET_NULL, null=True)
    members = models.ManyToManyField(CustomUser, related_name='projects', through='ProjectMembers')
    genre = models.ManyToManyField(Genre, related_name='projects', through='ProjectGenre')

    def add_leader_to_members(self):
        self.members.add(self.leader)

    def __str__(self):
        return self.name

class ProjectMembers(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('project', 'user'),)

class ProjectGenre(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

### Chat ########################################################

class Chat(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
