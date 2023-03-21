from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Niveau(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'niveau'
    
    def __str__(self):
        return self.name
    




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    niveau = models.OneToOneField(Niveau, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="profile", null=True, default="profile/default.png")
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username
    




class Categorie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categorie'

    def __str__(self):
        return self.name
    




class Article(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    recomendation = models.IntegerField(default=0)
    image = models.ImageField(upload_to="article/image", default="article/image/default.png")
    file = models.FileField(upload_to="article/file")
    description = models.TextField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'

    def __str__(self):
        return self.title


class Historique(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'historique'

    def __str__(self):
        return self.user.username + " --> " + self.article.title