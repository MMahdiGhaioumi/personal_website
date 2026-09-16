from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, verbose_name="نام کاربری")
    first_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="نام")
    last_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="نام خانوادگی")
    country = models.CharField(max_length=128, blank=True, null=True, verbose_name="کشور")
    city = models.CharField(max_length=128, blank=True, null=True, verbose_name="شهر")
    birth_date = models.DateField(verbose_name="تاریخ تولد", blank=True, null=True)
    image = models.ImageField(verbose_name="نگاره شخصی", upload_to="profile/", blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True, verbose_name="سن")
    information = models.TextField(blank=True, null=True, verbose_name="توضیحات کامل")
    short_information = models.TextField(blank=True, null=True, verbose_name="توضیحات کوتاه")
    resume = models.FileField(verbose_name="فایل رزومه", upload_to="resume/", blank=True, null=True)
    title_skills = models.CharField(verbose_name="عنوان برای مهارت ها", max_length=128)
    text_skills = models.TextField(blank=True, null=True, verbose_name="توضیحاتی درباره مهارت ها")

    is_admin = models.BooleanField(default=False, verbose_name="مدیر")

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self) -> str:
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_superuser(self):
        return self.is_admin

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"
