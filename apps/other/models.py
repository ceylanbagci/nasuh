from django.db import models
from django.utils.text import slugify
import transactions.service as trans_service


class Other(models.Model):
    title = models.CharField(max_length=60, verbose_name='Vargi')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        db_table = "other"

    def __str__(self):
        return self.title

    def _generate_unique_slug(self):
        unique_slug = slugify(self.title)
        num = 1
        while Other.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def get_stats(self):
        return trans_service.get_stats_other(instance=self)