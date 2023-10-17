from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
        name = models.CharField(max_length=50)
        price = models.DecimalField(max_digits=12, decimal_places=2)
        image = models.ImageField(max_length=200)
        release_date = models.DateField()
        lte_exists = models.BooleanField()
        slug = models.SlugField(max_length=60, unique=True, null=False)

        def save(self, *args, **kwargs):
                if not self.slug:
                        self.slug = slugify(self.name)
                return super().save(*args, **kwargs)

