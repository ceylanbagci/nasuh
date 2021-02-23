from django.db import models
from django.utils.text import slugify
#import transactions.service as trans_service
# Create your models here.

class Expense(models.Model):
    INCOME = 1
    EXPENSE = 2

    TYPE = (
        (INCOME, "Gelir"),
        (EXPENSE, "Gider"),
    )

    title = models.CharField(max_length=60, verbose_name='Başlık')
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.PositiveSmallIntegerField(choices=TYPE, verbose_name="Tür")
    office = models.ForeignKey('office.Office', on_delete=models.CASCADE,null=True, blank=True,
                             related_name="expenses", verbose_name="Ofis")
    tax = models.ForeignKey('tax.Tax', on_delete=models.CASCADE,null=True, blank=True,
                             related_name="expenses", verbose_name="Vergi")
    other = models.ForeignKey('other.Other', on_delete=models.CASCADE,null=True, blank=True,
                             related_name="expenses", verbose_name="Diğer")

    class Meta:
        db_table = "expense"

    def __str__(self):
        return self.title

    def _generate_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while Expense.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

#    def get_stats(self):
#        return trans_service.get_stats_expense(instance=self)

    def get_cname(self):
        class_name = 'Expense'
        return class_name


