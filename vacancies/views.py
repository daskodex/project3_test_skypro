from django.db.models import Count
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render

from vacancies.models import Specialty, Company, Vacancy


def main_view(request):
    specialties = Specialty.objects.annotate(num_vacancy=Count('vacancies')).all()
    companies = Company.objects.annotate(num_vacancy=Count('vacancies')).all()

    return render(request, 'index.html', {
        'specialties': specialties,
        'companies': companies
    })


"""
В целом мы получили рабочую вьюшку, и это отлично. Есть небольшая особенность
работы  шаблонов в Джанго. Во время запуска проекта Джанго "проходит" по всем 
папками templates в нашем проекте и собирает список файлов в них. Допустим у 
нас есть 2 папки:

/template/index.html
/app1/template/index.html  

В этом случае мы можем получить разные шаблоны для рендеренга, в зависимости
от приоритетности обхода (грубо говоря мы это не контролируем). 

Как решить поблему? Очень просто. Добавить под папку в директории templates:

/template/core/index.html
/app1/template/app1/index.html  

Тогда в нашей views ы напишем:

return render(request, 'core/index.html', {

"""


def jobs_views(request, specialty_code=None):
    if specialty_code:
        try:
            specialty = Specialty.objects.get(code=specialty_code)
        except:
            raise Http404()
        vacancies = Vacancy.objects.filter(specialty__code=specialty_code).all()
    else:
        specialty = None
        vacancies = Vacancy.objects.all()

    return render(request, 'vacancies.html', {
        'vacancies': vacancies,
        'specialty_code': specialty_code,
        'specialty': specialty,
    })


def company_view(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except:
        raise Http404()
    vacancies = Vacancy.objects.filter(company__id=company_id).all()

    return render(request, 'company.html', {
        'company': company,
        'vacancies': vacancies,
    })


def vacancy_view(request, job_id):
    try:
        vacancy = Vacancy.objects.get(id=job_id)
    except:
        raise Http404()

    return render(request, 'vacancy.html', {
        'vacancy': vacancy,
    })


def custom_handler404(request, exception):
    return HttpResponseNotFound('<br/><h1>Ошибка 404</h1><h2>Запрашиваемый ресурс не найден</h2>')


def custom_handler500(request):
    return HttpResponseServerError('<br/><h1>Ошибка 500</h1><h2>Ошибка запроса. Отказано в обработке</h2>')
