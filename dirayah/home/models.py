from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paymethod = models.CharField(max_length=50)
    answers = models.ManyToManyField('Answer', related_name='users_answered_questions', blank=True)
    problems_solved = models.ManyToManyField('Problem', related_name='users_solved_problems', blank=True)
    recommendations = models.ManyToManyField('Problem', related_name='users_recommended_problems', blank=True)

    def __str__(self):
        return self.user.username

class Problem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    id = models.AutoField(primary_key=True)
    difficulty = models.IntegerField()
    category = models.CharField(max_length=50)
    answers = models.ManyToManyField('Answer', related_name='answers', blank=True)
    teacher = models.ManyToManyField('Teacher', related_name='teacher', blank=True)
    comments = models.ManyToManyField('Comment',related_name='comments', blank=True)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True, blank=True, related_name='official_answer')

    def __str__(self):
        return self.title

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    id = models.AutoField(primary_key=True)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='problem')
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='answerer')

    def __str__(self):
        return self.answer

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    problems = models.ManyToManyField('Problem', related_name='problems', blank=True)
    answers = models.ManyToManyField('Answer', related_name='official_answers', blank=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    id = models.AutoField(primary_key=True)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE, related_name='parent_problem')
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='commenter')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return self.comment
