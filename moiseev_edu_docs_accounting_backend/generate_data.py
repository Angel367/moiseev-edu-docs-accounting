import os


import django
from faker import Faker

import random
from datetime import datetime, timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moiseev_edu_docs_accounting_backend.settings')
django.setup()
fake = Faker('ru_RU')
from moiseev_edu_docs_accounting_backend_app.models import Student, Teacher, Document
from django.contrib.auth.models import User

def create_students(num_students):
    for _ in range(num_students):
        first_name = fake.first_name()
        last_name = fake.last_name()
        # patronymic = fake.patronymic()
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=25)
        group = fake.random_element(elements=('A', 'B', 'C'))
        student_id_card = fake.unique.random_number(digits=8)
        try:
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                #patronymic=patronymic,
                birth_date=birth_date,
                group=group,
                student_id_card=student_id_card
            )
            print(f"Created student: {student}")
        except Exception as e:
            pass

def create_teachers(num_teachers):
    for _ in range(num_teachers):
        first_name = fake.first_name()
        last_name = fake.last_name()
       #  patronymic = fake.patronymic()
        birth_date = fake.date_of_birth(minimum_age=25, maximum_age=65)
        teacher_id_card = fake.unique.random_number(digits=8)
        try:
            teacher = Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                #patronymic=patronymic,
                birth_date=birth_date,
                teacher_id_card=teacher_id_card
            )
            print(f"Created teacher: {teacher}")
        except Exception as e:
            pass

def generate_document():
    title = fake.text(max_nb_chars=32)
    document_type = fake.random_element(elements=['Курсовая', 'Дипломная'])
    description = fake.text()
    created_at = fake.date_time_this_year()
    updated_at = created_at + timedelta(days=random.randint(1, 30))
    is_published = fake.boolean(chance_of_getting_true=50)
    author = Student.objects.order_by('?').first()
    kurator = Teacher.objects.order_by('?').first() if random.random() > 0.5 else None
    try:
        document = Document.objects.create(
            title=title,
            type=document_type,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            is_published=is_published,
            author=author,
            kurator=kurator
        )
        print(f"Created document: {document}")
    except Exception as e:
        pass


# Создание документов


# Создание студентов
create_students(50)

# Создание преподавателей
create_teachers(50)

for _ in range(50):
    generate_document()