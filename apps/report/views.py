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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.end_of_the_day(date=date)
    print(results)
    print(results['qs'])
    html_string = render_to_string('report/end_of.html',{'results':results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'),]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.end_of_the_month(date=date)
    print(results)
    print(results['qs'])
    html_string = render_to_string('report/end_of_month.html',{'results':results})
    print(html_string)
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'),]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.end_of_the_year(date=date)
    print(results)
    print(results['qs'])
    html_string = render_to_string('report/end_of.html',{'results':results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'),]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_case_list_report()
    html_string = render_to_string('report/case_list_report.html',{'results':results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'),]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_client_list_report()
    html_string = render_to_string('report/client_list_report.html',{'results':results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'),]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_partner_list_report()
    html_string = render_to_string('report/partner_list_report.html',{'results':results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'),]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_employee_list_report()
    html_string = render_to_string('report/employee_list_report.html',{'results':results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'),]
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

# @login_required
# def get_case_report(request,slug):
#     case = Case.objects.get(slug=slug)
#     fs = FileSystemStorage()
#     static_root = settings.STATICFILES_DIRS
#     results = trans_service.get_case_report(instance=case)
#     print(results)
#     html_string = render_to_string('report/end_of_case.html', {'results': results})
#     stylesheets = [CSS(static_root[0] + '/assets/css/report.css'), ]
#     file_name = case.title + '_hesap_hareketleri_' + str(datetime.date.today().strftime("%d.%m.%Y")) + '_.pdf'
#     HTML(string=html_string). \
#         write_pdf(fs.location + '/report/' + file_name, stylesheets=stylesheets)
#     fs = FileSystemStorage(fs.location + '/report')
#     with fs.open(fs.location + '/' + file_name) as pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         file_str = 'attachment; filename="' + file_name + '"'
#         response['Content-Disposition'] = file_str
#         os.remove(fs.location + '/' + file_name)
#         return response
#     return response

@login_required
def get_client_report(request,slug):
    client = Client.objects.get(slug=slug)
    fs = FileSystemStorage()
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_client_report(instance=client)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'), ]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_employee_report(instance=employee)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'), ]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_partner_report(instance=partner)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'), ]
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
    static_root = settings.STATICFILES_DIRS
    results = trans_service.get_single_expense_report(instance=expense)
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'), ]
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
    static_root = settings.STATICFILES_DIRS
    html_string = render_to_string('report/end_of.html', {'results': results})
    stylesheets = [CSS(static_root[0] + '/assets/css/report.css'), ]
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


import csv


#
# def get_case_report(request,slug):
#     case = Case.objects.get(slug=slug)
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="case.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['Dosya Sonu'])
#     writer.writerow(['Tarih', 'Gelir-Gider Türü', 'Açıklama', 'Miktar'])
#     results = trans_service.get_case_report(instance=case)
#     x = results['qs']
#     print(x)
#     # users = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
#     for trans in x:
#         writer.writerow([trans.date, trans.type, trans.description, trans.amount])
#
#     return response
#

from .utils import link_callback
from django.template.loader import get_template
from xhtml2pdf import pisa

def get_case_report(request,slug):
    case = Case.objects.get(slug=slug)
    results = trans_service.get_case_report(instance=case)
    template = get_template('report/end_of_case.html')
    html_string = render_to_string('report/end_of_case.html', {'results': results})
    html = template.render(results)
    print(html)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    pisa_status = pisa.CreatePDF(
        html_string, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



def render_pdf_view(request):
    template_path = 'user_printer.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=render_to_pdf)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response