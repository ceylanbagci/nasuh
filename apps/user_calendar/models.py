from django.db import models

# Create your models here.
class Event(models.Model):
    NOT_DONE = 1
    DONE = 2
    STATUS = (
        (NOT_DONE, "Hatırlatmaya Devam Et"),
        (DONE, "Bir Daha Hatırlatma"),
    )
    title = models.CharField(max_length=200, verbose_name='Başlık')
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name="events")
    backgroundColor = models.CharField(max_length=7, default="#3788d8")
    borderColor = models.CharField(max_length=7, default="#3788d8")
    start = models.DateTimeField(verbose_name='Başlangıç Zamanı')
    end = models.DateTimeField(verbose_name='Bitiş Zamanı')
    editable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    client = models.ForeignKey('case.Client',on_delete=models.SET_NULL,blank=True,null=True,related_name='events',verbose_name='Müvekkil')
    case = models.ForeignKey('case.Case',on_delete=models.SET_NULL,blank=True,null=True,related_name='events',verbose_name='Dosya')
    status = models.PositiveSmallIntegerField(choices=STATUS, default=NOT_DONE,verbose_name='Durum')

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.title