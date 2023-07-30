from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):# در کل دو تا تابع به نام های create_user,create_superuser دارد
    def create_user(self, phone_number, email, full_name, password):
        if not phone_number:
            raise ValueError('user must have phone number')

        if not email:
            raise ValueError('user must have email')

        if not full_name:
            raise ValueError('user must have full name')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email), full_name=full_name)#ایمیل را باید اینگونه بدهیم تا برایمان اعتبارسنجی بکند
        user.set_password(password) # برای هش کردن پسورد همیشه باید اینگونه بنویسیم
        user.save(using= self._db)
        return user

    def create_superuser(self, phone_number, email, full_name, password):
        user = self.create_user(phone_number, email, full_name, password)
        user.is_admin= True
        user.save(using=self._db)
        return user


