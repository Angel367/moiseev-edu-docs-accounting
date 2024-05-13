from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField()
    group = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student_id_card = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.last_name} {self.student_id_card}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    patronymic = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher_id_card = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('Курсовая', 'Курсовая'),
        ('Дипломная', 'Дипломная')
    ]
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES)
    description = models.TextField(null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    file = models.FileField(upload_to='documents/', blank=False, null=False)
    author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='document', null=True, blank=True)

    def __str__(self):
        return self.title
