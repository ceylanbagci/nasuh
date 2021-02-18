from django.db import models
import datetime
from django.db.models import Sum, Q, Count



class Transaction(models.Model):
    INCOME = 1
    SPENT = 2
    TRANSACTION_TYPES = (
        (INCOME, "Gelir"),
        (SPENT, "Gider"),
    )

    amount = models.DecimalField(max_digits=8, decimal_places=2,verbose_name='Tutar')
    type = models.PositiveSmallIntegerField(choices=TRANSACTION_TYPES, default=SPENT,verbose_name='Tür')
    date = models.DateField(null=True, blank=True,verbose_name='Tarih')
    created_at = models.DateTimeField(auto_now_add=True)
    expense = models.ForeignKey('expense.Expense',on_delete=models.CASCADE,related_name='transactions',verbose_name='Gelir Gider')
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    employee = models.ForeignKey('office.Employee', null=True, blank=True, on_delete=models.CASCADE,related_name='transactions',verbose_name='Çalışan')
    case = models.ForeignKey('case.Case', null=True, blank=True, on_delete=models.CASCADE,related_name='transactions',verbose_name='Dosya')

    class Meta:
        db_table = "transaction"


    def __str__(self):
        return "%s %s %s"%(self.expense.title,self.amount,self.type)

    def save(self,*args, **kwargs):
        if not self.date:
            self.date = datetime.date.today()
        if self.type == Transaction.SPENT:
            self.amount = self.amount*(-1)
        super().save(*args, **kwargs)

    def get_cname(self):
        class_name = 'Transaction'
        return class_name
