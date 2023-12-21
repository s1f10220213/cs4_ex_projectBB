from django.db import models

# Create your models here.


# class User(models.Model):
#     user_id = models.CharField(max_length=225, unique=True)
#     user_name = models.TextField()
#     user_password = models.ForeignKey(Listinfo, on_delete=models.CASCADE, related_name="list_info", null=True)

#     def __str__(self):
#         return self.user_name


class Project_member(models.Model):
    project_id = models.ForeignKey(Project_detail, on_delete=models.CASCADE, related_name="id", null=True) #　プロジェクトのデータベースにアクセス
    userList_id = models.ForeignKey(, on_delete=models.CASCADE, related_name="", null=True) #　参加メンバーのデータベースにアクセス

class Project_detail(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=25)
    genre_id = models.ForeignKey(, on_delete=models.CASCADE, related_name="", null=True) #　募集ジャンルのデータベースにアクセス
    explain = models.CharField(max_length=255)
    leader_id = models.ForeignKey(, on_delete=models.CASCADE, related_name="", null=True) #　リーダーのid

class Project_Chatroom(models.Model):
    id = models.IntegerField()
    project_id = models.IntegerField()
    name = models.CharField(max_length=15)

class Project_Genre(models.Model):
    project_id = models.ForeignKey(, on_delete=models.CASCADE, related_name="", null=True) #　募集ジャンルのデータベースにアクセス
    genre_id = models.ForeignKey(, on_delete=models.CASCADE, related_name="", null=True)

class User_genre(models.Model):
    user_id = models.ForeignKey(,)
    genre_id = models.ForeignKey(,)

class Genres(models.Model):
    genre_id = models.IntegerField()
    genre_name = models.CharField(max_length=10)


# class Listinfo(models.Model):
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="Genre")
#     list_num = models.IntegerField()
#     list_name = models.CharField(max_length=225, null=True)

# class Word(models.Model):
#     word = models.CharField(max_length=255)
#     meaning = models.TextField()
#     belonging_list = models.ForeignKey(Listinfo, on_delete=models.CASCADE, related_name="list_info", null=True)

# class Test(models.Model):
#     word = models.CharField(max_length=225)
#     option1 = models.CharField(max_length=225)
#     option2 = models.CharField(max_length=225)
#     option3 = models.CharField(max_length=225, null=True)
#     option4 = models.CharField(max_length=225, null=True)
#     answer = models.CharField(max_length=225)
#     correct_answer = models.CharField(max_length=225)