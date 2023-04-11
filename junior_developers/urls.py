"""junior_developers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

"""
В строке # from django.contrib import admin нет никакой ошибки, однако если 
мы что-то комментируем, и работой над проектом занимается несколько человек,
желательно написать почему закомменитрован рабочий кусок кода.

Например:

# отключили админку, т.к. в проекте ее не используем.
# from django.contrib import admin

"""

from vacancies.views import (
    main_view, jobs_views, company_view, vacancy_view, custom_handler404, custom_handler500
)

"""
Строка выше написана правильна с точки зрения работы, однако ее можно улучшить.
Согласно PEP8 (стандарт оформления кода), длина строки должна быть меньше 80 
символов. Это повышает читаемость 

Например мы можем сделать вот такое решение:

from vacancies.views import (
    main_view,
    jobs_views,
    company_view,
    vacancy_view,
    ...
)

"""

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/<str:specialty_code>', jobs_views, name='vacancies'),
    path('vacancies', jobs_views, name='vacancies_all'),
    path('company/<int:company_id>', company_view, name='company'),
    path('vacancy/<int:job_id>', vacancy_view, name='vacancy'),
]

"""
1.Хорошо выполнена структура путей, читаемые имена views. Согласно тех заданию
в проекте не хватает 
– Вакансии по специализации /vacancies/cat/frontend

2.Так же согласно ТЗ, у нас должен быть путь
– Карточка компании  /companies/345

Фактически мы имеем:
path('company/<int:company_id>', company_view, name='company'),

Это означает, что наш код не соответствует заданию, что усложнит написание
проекта и работу например тестировщиков или авто тестов.

3.Аналогично с вакансиями, мы должны иметь путь:
– Одна вакансия /vacancies/22

Фактически имеем:
path('vacancy/<int:job_id>', vacancy_view, name='vacancy'),

Желательно привести наши пути в соотвтетствие с ТЗ
"""

handler404 = custom_handler404
handler500 = custom_handler500
