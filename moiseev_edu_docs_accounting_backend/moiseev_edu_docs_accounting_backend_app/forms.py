from django import forms
from .models import *


class RussianDateInput(forms.DateInput):
    input_type = 'date'
    format = '%d.%m.%Y'


class StudentForm(forms.ModelForm):
    birth_date = forms.DateField(widget=RussianDateInput)

    class Meta:
        model = Student
        fields = ['last_name', 'first_name', 'patronymic', 'birth_date', 'group', 'student_id_card']


class TeacherForm(forms.ModelForm):
    birth_date = forms.DateField(widget=RussianDateInput)

    class Meta:
        model = Teacher
        fields = ['last_name', 'first_name', 'patronymic', 'birth_date', 'teacher_id_card']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'type', 'file', 'author']  # Assuming 'teacher' is not needed as it's a duplicate ForeignKey


class DocumentFilterForm(forms.Form):
    year = forms.IntegerField(label='Year', required=False)
    student_lastname = forms.ModelChoiceField(label='Student Last Name',
                                              queryset=Student.objects.all(),
                                              required=False,
                                              to_field_name='last_name',  # Добавляем to_field_name
                                              widget=forms.Select(
                                                  attrs={'class': 'form-select'}))  # Добавляем класс формы
    title_contains = forms.CharField(label='Title Contains', max_length=100, required=False)
