from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

class User(AbstractBaseUser):# this modele inheriate from abstractbaceuser that has some default atteribute like username for user model
    email = models.CharField(max_length=255, unique=True) # for user cannot enter the repetitious email we set unique=True
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FILED = 'phone_number' # اعتبار سنجی کاربر با شماره تلفن و این شماره تلفن باید یونیک باشد
    REQUIRED_FIELDS = ['email'] # this code just use when in terminal we enter python manage.py createsuperuser for get some info from user


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):# مشخص می کند کاربر به مدل ها دسترسی دارد یا نه
        return True

    @property
    def is_staff(self):#کاربر هایی که اجازه دارند وارد ادمین پلن شوند
        return self.is_admin