from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.conf import settings
from datetime import date
import transactions.service as trans_service
from django.http import JsonResponse, HttpResponse
import datetime
from case.models import Case,Client,Partner
import os
from expense.models import Expense
from office.models import Employee
from django.contrib.auth.decorators import login_required

@login_required
def end_of_the_day(request,date=datetime.date.today()):
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.end_of_the_day(date=date)
    html_string = render_to_string('report/end_of.html',{'results':results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'),]
    file_name = 'gun_sonu_'+str(datetime.date.today().strftime("%d.%m.%Y"))+'_.pdf'
    HTML(string=html_string).\
          write_pdf(fs.location+'/report/'+file_name,stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location +'/report')
    with fs.open(fs.location + '/'+file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="'+file_name+'"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def end_of_the_month(request,date=datetime.date.today()):
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.end_of_the_month(date=date)
    html_string = render_to_string('report/end_of.html',{'results':results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'),]
    file_name = 'ay_sonu_'+str(datetime.date.today().strftime("%d.%m.%Y"))+'_.pdf'
    HTML(string=html_string).\
          write_pdf(fs.location+'/report/'+file_name,stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location +'/report')
    with fs.open(fs.location + '/'+file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="'+file_name+'"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def end_of_the_year(request,date=datetime.date.today()):
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.end_of_the_year(date=date)
    html_string = render_to_string('report/end_of.html',{'results':results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'),]
    file_name = 'yıl_sonu_'+str(datetime.date.today().strftime("%d.%m.%Y"))+'_.pdf'
    HTML(string=html_string).\
          write_pdf(fs.location+'/report/'+file_name,stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location +'/report')
    with fs.open(fs.location + '/'+file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="'+file_name+'"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_case_list_report(request):
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_case_list_report()
    html_string = render_to_string('report/case_list_report.html',{'results':results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'),]
    file_name = 'dava_dosyaları_'+str(datetime.date.today().strftime("%d.%m.%Y"))+'_.pdf'
    HTML(string=html_string).\
          write_pdf(fs.location+'/report/'+file_name,stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location +'/report')
    with fs.open(fs.location + '/'+file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="'+file_name+'"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_client_list_report(request):
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_client_list_report()
    html_string = render_to_string('report/client_list_report.html',{'results':results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'),]
    file_name = 'müvekkil_listesi_'+str(datetime.date.today().strftime("%d.%m.%Y"))+'_.pdf'
    HTML(string=html_string).\
          write_pdf(fs.location+'/report/'+file_name,stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location +'/report')
    with fs.open(fs.location + '/'+file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="'+file_name+'"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_partner_list_report(request):
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_partner_list_report()
    html_string = render_to_string('report/partner_list_report.html',{'results':results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'),]
    file_name = 'ortak_listesi_'+str(datetime.date.today().strftime("%d.%m.%Y"))+'_.pdf'
    HTML(string=html_string).\
          write_pdf(fs.location+'/report/'+file_name,stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location +'/report')
    with fs.open(fs.location + '/'+file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="'+file_name+'"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_employee_list_report(request):
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_employee_list_report()
    html_string = render_to_string('report/employee_list_report.html',{'results':results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'),]
    file_name = 'çalışan_listesi_'+str(datetime.date.today().strftime("%d.%m.%Y"))+'_.pdf'
    HTML(string=html_string).\
          write_pdf(fs.location+'/report/'+file_name,stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location +'/report')
    with fs.open(fs.location + '/'+file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="'+file_name+'"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def report_list(request):
    return render(request, 'report/report_list.html')

@login_required
def get_with_day(request):
    if request.method == "POST":
        date = datetime.datetime.strptime(request.POST['date'], '%d/%m/%Y')
        return end_of_the_day(request,date=date)
    else:
        return render(request, 'report/new_form_input.html')

@login_required
def get_with_month(request):
    if request.method == "POST":
        date = datetime.datetime.strptime(request.POST['date'], '%m/%Y')
        return end_of_the_month(request,date=date)
    else:
        return render(request, 'report/new_form_input.html')

@login_required
def get_with_year(request):
    if request.method == "POST":
        date = datetime.datetime.strptime(request.POST['date'], '%Y')
        return end_of_the_year(request,date=date)
    else:
        return render(request, 'report/new_form_input.html')

@login_required
def get_case_report(request,slug):
    case = Case.objects.get(slug=slug)
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_case_report(instance=case)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'), ]
    file_name = case.title + '_hesap_hareketleri_' + str(datetime.date.today().strftime("%d.%m.%Y")) + '_.pdf'
    HTML(string=html_string). \
        write_pdf(fs.location + '/report/' + file_name, stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location + '/report')
    with fs.open(fs.location + '/' + file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="' + file_name + '"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_client_report(request,slug):
    client = Client.objects.get(slug=slug)
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_client_report(instance=client)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'), ]
    file_name = client.full_name + '_hesap_hareketleri_' + str(datetime.date.today().strftime("%d.%m.%Y")) + '_.pdf'
    HTML(string=html_string). \
        write_pdf(fs.location + '/report/' + file_name, stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location + '/report')
    with fs.open(fs.location + '/' + file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="' + file_name + '"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_employee_report(request,slug):
    employee = Employee.objects.get(slug=slug)
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_employee_report(instance=employee)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'), ]
    file_name = employee.full_name + '_hesap_hareketleri_' + str(datetime.date.today().strftime("%d.%m.%Y")) + '_.pdf'
    HTML(string=html_string). \
        write_pdf(fs.location + '/report/' + file_name, stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location + '/report')
    with fs.open(fs.location + '/' + file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="' + file_name + '"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_partner_report(request,slug):
    partner = Partner.objects.get(slug=slug)
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_partner_report(instance=partner)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'), ]
    file_name = partner.full_name + '_hesap_hareketleri_' + str(datetime.date.today().strftime("%d.%m.%Y")) + '_.pdf'
    HTML(string=html_string). \
        write_pdf(fs.location + '/report/' + file_name, stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location + '/report')
    with fs.open(fs.location + '/' + file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="' + file_name + '"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_single_expense_report(request,slug):
    expense = Expense.objects.get(slug=slug)
    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    results = trans_service.get_single_expense_report(instance=expense)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'), ]
    file_name = expense.title + 'icin_hesap_hareketleri_' + str(datetime.date.today().strftime("%d.%m.%Y")) + '_.pdf'
    HTML(string=html_string). \
        write_pdf(fs.location + '/report/' + file_name, stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location + '/report')
    with fs.open(fs.location + '/' + file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="' + file_name + '"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response

@login_required
def get_expense_report(request):
    coming_url = request.META.get("HTTP_REFERER")
    if 'case' in coming_url:
        results = trans_service.get_expense_report(object='case')
    elif 'office' in coming_url:
        results = trans_service.get_expense_report(object='office')
    elif 'tax' in coming_url:
        results = trans_service.get_expense_report(object='tax')
    elif 'other' in coming_url:
        results = trans_service.get_expense_report(object='other')
    elif 'expense_list_all' in coming_url:
        results = trans_service.get_expense_report(object='expense')

    fs = FileSystemStorage()
    static_root = settings.STATIC_ROOT
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root + '/assets/css/report.css'), ]
    file_name = 'gelir-gider_turu_hesap_hareketleri_' + str(datetime.date.today().strftime("%d.%m.%Y")) + '_.pdf'
    HTML(string=html_string). \
        write_pdf(fs.location + '/report/' + file_name, stylesheets=stylesheets)
    fs = FileSystemStorage(fs.location + '/report')
    with fs.open(fs.location + '/' + file_name) as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        file_str = 'attachment; filename="' + file_name + '"'
        response['Content-Disposition'] = file_str
        os.remove(fs.location + '/' + file_name)
        return response
    return response
