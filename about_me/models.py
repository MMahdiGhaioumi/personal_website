from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    title = models.CharField(max_length=128, unique=True, verbose_name='نام سرویس')
    body = models.TextField(max_length=1025, verbose_name='توضیح', help_text="توضیح کوتاه اما مفید و تاثیرگذار")
    icon = models.FileField(verbose_name='آیکون سرویس', upload_to='services/icons', validators=[
        FileExtensionValidator(['svg'])
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} -- {self.body[:20]}"

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمت'
        ordering = ('title',)


class Skill(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='نام مهارت')
    persent = models.PositiveSmallIntegerField(verbose_name="درصد مهارت", validators=[
        MinValueValidator(0),
        MaxValueValidator(100),
    ])

    def __str__(self):
        return f"{self.name} -- {self.persent}"

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت'
        ordering = ('-persent',)


class Resume(models.Model):
    class Place(models.TextChoices):
        EDUCATION = 'edu', 'Education'
        EXPERIENCE = 'exp', 'Experience'

    place = models.CharField(verbose_name="انتخاب حالت", choices=Place, max_length=50)
    title = models.CharField(verbose_name="عنوان", max_length=128)
    place_name = models.CharField(verbose_name="نام", max_length=128)
    description = models.TextField(verbose_name="توضیحات", unique=True)
    start_date = models.DateField(verbose_name="تاریخ شروع", blank=True, null=True)
    end_date = models.DateField(verbose_name="تاریخ پایان", blank=True, null=True)

    class Meta:
        ordering = ('-start_date', '-end_date')
        verbose_name = "رزومه"
        verbose_name_plural = "رزومه"

    def __str__(self):
        return self.title
