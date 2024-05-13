from django.shortcuts import render, redirect
from .forms import *


def student(request):
    return render(request, 'student/student.html')


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/student_create.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})


def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return redirect('page_404')
    return render(request, 'student/student_detail.html', {'student': student})


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student/student_delete.html', {'student': student})


def teacher(request):
    return render(request, 'teacher/teacher.html')


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher/teacher_create.html', {'form': form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})


def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return redirect('page_404')
    return render(request, 'teacher/teacher_detail.html', {'teacher': teacher})


def teacher_delete(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teacher/teacher_delete.html', {'teacher': teacher})


def document(request):
    return render(request, 'document/document.html')

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'document/document_create.html', {'form': form})


def document_list(request):
    documents = Document.objects.all()
    filter_form = DocumentFilterForm(request.GET)
    if filter_form.is_valid():
        year = filter_form.cleaned_data.get('year')
        student_lastname = filter_form.cleaned_data.get('student_lastname')
        title_contains = filter_form.cleaned_data.get('title_contains')
        if year:
            documents = documents.filter(created_at__year=year)
        if student_lastname:
            documents = documents.filter(author__last_name=student_lastname)
        if title_contains:
            documents = documents.filter(title__icontains=title_contains)
    return render(request, 'document/document_list.html', {'documents': documents, 'filter_form': filter_form})


def document_detail(request, pk):
    try:
        document = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return redirect('page_404')
    return render(request, 'document/document_detail.html', {'document': document})


def document_delete(request, pk):
    document = Document.objects.get(pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    return render(request, 'document/document_delete.html', {'document': document})


def main_page(request):
    return render(request, 'index.html')


def page_404(request):
    return render(request, '404.html')
