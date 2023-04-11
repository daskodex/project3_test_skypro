from django.db import models

"""
Желательно писать комментарии у моделей, и описывать какой функционал она несет
"""
class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

""" 
1.В тех задании написано название поля:
– Название (name)
В модели используется:
title = models.CharField(max_length=20)

2.Кстати наверняка есть компании которые имеют название больше 20 символов.

3.Вместо поля id можно использовать встроенный первичный ключ pk, это 
немного упростит логику работы


"""

class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    posted = models.DateField()

"""
Модель получилась вполне рабоая, но можно немного ее улучшить.

1.В ТЗ нас просят сделать поле модели:

– Опубликовано (published_at)

однако мы имеем поле: 

    posted = models.DateField()

Что это означает? Что в какой то момент вы, ваш коллега разработчик
или тестировщик не обнаружит нужное в тех задании поле и не будет знать
как ему поступить в этой ситуации.

2.Немного про поля salary_min и salary_max, для таких цифр как например 
зарплаты есть более удобный тип PositiveIntegerField

3.В поле models.DateField() лучше установить параметр auto_now или auto_add_now,
это позволит ускорить заполнение полей (а еще это даст данные для seo оптимизатора
при формировании sitemap.xml файла) 

4.Еще у нас есть такой классный параметр как verbouse_name=, он нужен для описания
поле для нас разработчков и в админке. Например:

salary_max = models.IntegerField(verbose_name='Зарплата: максимальная')

"""



