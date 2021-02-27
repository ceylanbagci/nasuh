from django.db import models
from django.utils.text import slugify
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Başlık')
    backgroundColor = models.CharField(max_length=7, default="#3699ff")
    borderColor = models.CharField(max_length=7, default="#3699ff")
    start = models.DateTimeField(verbose_name='Başlangıç Zamanı')
    end = models.DateTimeField(verbose_name='Bitiş Zamanı')
    editable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    client = models.ForeignKey('case.Client',on_delete=models.SET_NULL,blank=True,null=True,related_name='events',verbose_name='Müvekkil')
    case = models.ForeignKey('case.Case',on_delete=models.SET_NULL,blank=True,null=True,related_name='events',verbose_name='Dosya')
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True, verbose_name="Açıklama")
    is_read = models.BooleanField(default=False)

    class Meta:
        db_table = "event"

    def __str__(self):
        return self.title

    def _generate_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)