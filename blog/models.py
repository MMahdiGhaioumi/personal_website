from typing import Any

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.text import slugify


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='نام تگ')
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ"
        ordering = ['name']


class Comment(models.Model):
    name = models.CharField(verbose_name="نام کاربر", max_length=255)
    email = models.EmailField(verbose_name="ایمیل", null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="پاسخ به کاربر", related_name='replies',
                               blank=True, null=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments", verbose_name="مقاله")
    body = models.TextField(verbose_name="متن")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(verbose_name="وضعیت", default=False)

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}-- {self.email} --{self.body[:30]}"

    class Meta:
        verbose_name = "دیدگاه"
        verbose_name_plural = "دیدگاه"
        ordering = ['-created_at']


class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="کاربر", related_name='posts')
    title = models.CharField(max_length=255, unique=True, verbose_name="نام مقاله")
    tags = models.ManyToManyField(Tag, verbose_name="تگ ها", related_name='posts', blank=True)
    body = models.TextField(verbose_name="متن و محتوای مقاله")
    image = models.ImageField(upload_to='blog', blank=True, null=True, verbose_name="نگاره")
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}--{self.body[:30]}"

    def get_absolute_url(self):
        url = reverse_lazy('blog:blog_detail', kwargs={'slug': self.slug})
        return url

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله"
        ordering = ['-updated_at', '-id']
