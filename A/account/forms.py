from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    #چون ما در مدل ها پسوردمان را مشخص نکردیم اینجا مشخص میکنیم
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    #این تابع درست بودن دو تا پسورد وارد شده را برسی میکند
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dosent match')
        return cd['password2'] # حتما باید پسورد دو را برگرداند

    #چون در اینجا ما پسورد را نوشتیم باید به تابع سیو بگویم یک لحظه وایسا تا ما پسورد ها را هم سیو کنیم
    def save(self, commit=True):
        user = super().save(commit=False)# کامیت برابر فالس یعنی کمی وایسا
        user.set_password(self.cleaned_data['password1'])#اون پسورد هش شده را بگیر فرقی نمیکند پسوردیک یا پسورددو را بدهیم
        if commit:
            user.save()
        return user #در آخر حتما باید یوزر را برگردانیم


class UserChangeForm(forms.ModelForm):#این کلاس اطلاعات وارد شده کاربر را تغییر میدهد
    # فقط در اون مسیر داده شده می توان پسورد را عوض کرد
    password = ReadOnlyPasswordHashField(help_text="you cant change password using <a href = \"../password/\">this form</a>")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')# در اینجا پسورد و last_login در مدل مان نداریم اما چون داخل AbstractBaseUser هست میتوان اینجا بنویسیمشان