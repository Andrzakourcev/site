from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Cars.Status.PUBLISHED)





class Cars(models.Model):

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
          ]

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True) #blank - поле необязательно для заполнения
    time_create = models.DateTimeField(auto_now_add=True) #auto_now_add - автоматические заполняет запись в момент первого появления
    time_update = models.DateTimeField(auto_now=True) #auto_now_add - автоматические заполняет запись в момент первого появления
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')
    tag = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    ceo = models.OneToOneField('Ceo', blank=True, on_delete=models.SET_NULL, null=True, related_name='cars')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug':self.slug})

    def __str__(self):
        return self.tag

class Ceo(models.Model):
    fio = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def __str__(self):
        return self.fio