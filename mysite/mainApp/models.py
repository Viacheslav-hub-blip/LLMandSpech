from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_sucsess = models.BooleanField(default=False)


class StudentModel(models.Model):
    name = models.CharField(max_length=80)
    sex = models.CharField(max_length=15)
    age = models.IntegerField()
    group = models.ForeignKey(to='GroupModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GroupModel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
