from django.db import models
from django.contrib.auth import get_user_model


class SocialMedia(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="کاربر",
                             related_name="social_medias")
    name = models.CharField(max_length=50, verbose_name="نام")
    link = models.URLField(verbose_name="لینک", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پیامرسان ها و راه های ارتباطی"
        verbose_name_plural = "پیامرسان ها و راه های ارتباطی"
        ordering = ["name"]
        # constraints = [
        #     models.UniqueConstraint(fields=["name", "link"], name="unique_link_in_a_social_media"),
        # ]


class Phone(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="کاربر", related_name="phones")
    operator_name = models.CharField(max_length=50, verbose_name="نام اپراتور(سیمکارت)")
    phone = models.CharField(verbose_name="شماره همراه", unique=True, max_length=13)

    def __str__(self):
        return f"{self.operator_name} -- {self.phone}"

    class Meta:
        verbose_name = "شماره همراه"
        verbose_name_plural = "شماره همراه"
        ordering = ["operator_name"]


class Email(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="کاربر", related_name="emails")
    email = models.EmailField(verbose_name="آدرس ایمیل", unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "آدرس ایمیل"
        verbose_name_plural = "آدرس ایمیل"


class Address(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="کاربر", related_name="addresses")
    address = models.TextField(unique=True, verbose_name="نشانی")

    def __str__(self):
        return f"{self.user} -- {self.address}"

    class Meta:
        verbose_name = "نشانی"
        verbose_name_plural = "نشانی"


class Message(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام")
    email = models.EmailField(verbose_name="آدرس ایمیل")
    subject = models.CharField(max_length=255, verbose_name="موضوع")
    text = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -- {self.subject}"

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام"
