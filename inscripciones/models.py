# models.py
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
class Character(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="characters/")
class VerseCard(models.Model):
    reference = models.CharField(max_length=50)   # Ej. "Hechos 1:8"
    excerpt = models.CharField(max_length=255)    # Texto breve que aparece en la ficha
    full_text = models.TextField()                # Versículo completo

    def __str__(self):
        return self.reference
class GeneralQuestion(models.Model):
    text = models.CharField(max_length=255)

class GeneralOption(models.Model):
    question = models.ForeignKey(GeneralQuestion, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
