from django.conf import settings
from django.db import models
from django.utils import timezone

# class Blog(models.Model):
    
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogger', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255, verbose_name=u"Название блога")
#     description = models.CharField(max_length=1024, verbose_name=u"Описание")
#     pub_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Дата создания")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = u"Блог"
#         verbose_name_plural = u"Блоги"
#         ordering = ('pub_date', )

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name=u"post title")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    blog = models.ForeignKey(Blog, related_name='blogs', on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True, verbose_name=u"last update")
    likes = models.PositiveIntegerField(default=0)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = u"Пост"
    #     verbose_name_plural = u"Посты"