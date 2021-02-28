from django.db import models
from django.utils.text import slugify
from case.models import*
from django.db import models
import core.helper as hlp
from expense.models import Expense

class Office(models.Model):
    title = models.CharField(max_length=60, verbose_name='Başlık')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        db_table = "office"

    def __str__(self):
        return self.title

    def _generate_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while Office.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)


    def get_total_Employee(self):
        lenght = len(Partner.objects.all())
        return lenght

    def get_stats(self):
        import transactions.service as trans_service
        return trans_service.get_stats_office(instance=self)


class Employee(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Ad')
    last_name = models.CharField(max_length=20, verbose_name='Soyad')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefon')
    address = models.CharField(max_length=20, blank=True, null=True, verbose_name='Adres')
    email = models.CharField(max_length=50, blank=True, null=True, verbose_name='Email')
    city = models.ForeignKey('core.City', null=True, blank=True, on_delete=models.SET_NULL,
                             related_name="employees", verbose_name="İl")
    district = models.ForeignKey('core.District', null=True, blank=True, on_delete=models.SET_NULL,
                                 related_name="employees", verbose_name="İlçe")
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    salary = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Maaş')
    office = models.ForeignKey(Office, on_delete=models.CASCADE,
                             related_name="employees", verbose_name="Ofis")

    class Meta:
        db_table = "employee"

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def _generate_unique_slug(self):
        unique_slug = slugify(self.full_name)
        num = 1
        while Employee.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def get_stats(self):
        import transactions.service as trans_service
        return trans_service.get_stats_employee(instance=self)

    def get_cname(self):
        class_name = 'Employee'
        return class_name
