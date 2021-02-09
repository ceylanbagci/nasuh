import django_filters
from django import forms
from django.db.models import Q
from .models import *


class CaseFilter(django_filters.FilterSet):
    text_search = django_filters.CharFilter(method='my_text_search', label="Arama", widget=forms.TextInput(attrs={'placeholder': 'Ara...', 'class': ' form-control custom-shadow custom-radius bg-white'}))


    sort = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('date', 'date'),
        ),
        field_labels={
            'title': 'Ada Göre',
            '-title': 'Ada Göre (azalan)',
            'date': 'Tarihe Göre',
            '-date': 'Tarihe Göre (azalan)',
        },
    )

    STATUS_CHOICES = (
        (1, 'Açık'),
        (2, 'Olumsuz'),
        (3, 'İstinaf'),
        (4, 'Yargıtay'),
        (5, 'Derdest'),
        (6, 'Hitam Olumlu'),
        (7, 'Hitam Olumsuz'),
    )

    status = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES
    )

    class Meta:
        model = Case
        fields = ['text_search',"sort",'status']

    def __init__(self,data=None, queryset=None, *, request=None, prefix=None):
        super(CaseFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['text_search'].field.widget.attrs.update({'class': ' form-control'})
        self.filters['sort'].field.widget.attrs.update({'class': ' custom-select custom-select-set form-control bg-white custom-shadow custom-radius'})
        self.filters["sort"].field.empty_label = "Sırala"
        self.filters['status'].field.widget.attrs.update({'class': ' custom-select custom-select-set form-control bg-white custom-shadow custom-radius'})
        self.filters["status"].field.empty_label = "Durum"

    def my_text_search(self, queryset, name, value):
        return Case.objects.filter(
            Q(title__icontains=value) | Q(case_id__icontains=value) |
            Q(client__first_name__icontains=value) | Q(client__last_name__icontains=value) |
            Q(partner__first_name__icontains=value) | Q(partner__last_name__icontains=value) |
            Q(city__name__icontains=value) | Q(district__name__icontains=value) |
            Q(client__city__name__icontains=value) | Q(client__district__name__icontains=value) |
            Q(partner__city__name__icontains=value) | Q(partner__district__name__icontains=value)
        )

class ClientFilter(django_filters.FilterSet):
    text_search = django_filters.CharFilter(method='my_text_search', label="Arama", widget=forms.TextInput(attrs={'placeholder': 'Ara...', 'class': ' form-control custom-shadow custom-radius bg-white'}))


    sort = django_filters.OrderingFilter(
        fields=(
            ('first_name', 'first_name'),
        ),
        field_labels={
            'first_name': 'Ada Göre',
            '-first_name': 'Ada Göre (azalan)',
        },
    )



    class Meta:
        model = Client
        fields = ['text_search',"sort"]

    def __init__(self,data=None, queryset=None, *, request=None, prefix=None):
        super(ClientFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['text_search'].field.widget.attrs.update({'class': ' form-control'})
        self.filters['sort'].field.widget.attrs.update({'class': ' custom-select custom-select-set form-control bg-white custom-shadow custom-radius'})
        self.filters["sort"].field.empty_label = "Sırala"

    def my_text_search(self, queryset, name, value):
        return Client.objects.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value) |
            Q(email__icontains=value) | Q(phone__icontains=value) |
            Q(city__name__icontains=value) | Q(district__name__icontains=value) |
            Q(description__icontains=value)
        )

class PartnerFilter(django_filters.FilterSet):
    text_search = django_filters.CharFilter(method='my_text_search', label="Arama", widget=forms.TextInput(attrs={'placeholder': 'Ara...', 'class': ' form-control custom-shadow custom-radius bg-white'}))


    sort = django_filters.OrderingFilter(
        fields=(
            ('first_name', 'first_name'),
        ),
        field_labels={
            'first_name': 'Ada Göre',
            '-first_name': 'Ada Göre (azalan)',
        },
    )



    class Meta:
        model = Partner
        fields = ['text_search',"sort"]

    def __init__(self,data=None, queryset=None, *, request=None, prefix=None):
        super(PartnerFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
        self.filters['text_search'].field.widget.attrs.update({'class': ' form-control'})
        self.filters['sort'].field.widget.attrs.update({'class': ' custom-select custom-select-set form-control bg-white custom-shadow custom-radius'})
        self.filters["sort"].field.empty_label = "Sırala"

    def my_text_search(self, queryset, name, value):
        return Partner.objects.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value) |
            Q(email__icontains=value) | Q(phone__icontains=value) |
            Q(city__name__icontains=value) | Q(district__name__icontains=value) |
            Q(description__icontains=value)
        )
