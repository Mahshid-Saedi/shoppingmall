from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm
from .models import User, OtpCode

@admin.register(OtpCode)#اسم مدلمان را بهش میدهیم
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


#اضافه کرد فرم هایمان به پنل ادمین
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm # چون دو تا فرم داریم این یکی را داخل add_form مینویسیم

    list_display = ('email', 'phone_number', 'is_admin') # چه چیز هایی باید در پنل ادمین نمایش داده شود
    list_filter = ('is_admin',) # بر چه اساسی نمایش کاربر ها را فیلتر کند

    #به ما اجازه میدهد مجموعه ای از input ها را به صورت یکجا نمایش دهد
    fieldsets = (
        (None, {'fields':('email', 'phone_number', 'full_name', 'password')}),# ابتدا یک عنوان می گیرد بعد یک دیکشنری از فیلد ها که کلیدش را fields میگذاریم
        ('permission', {'fields':('is_active', 'is_admin', 'last_login')}),
    )

    #چون دو تا فرم داشتیم برای اون یکی داخل add_fieldsets مینویسیم
    add_fieldsets = (
        (None, {'fields':('phone_number', 'email', 'full_name', 'password1', 'password2')}),
    )

    search_fields = ('email', 'full_name')#بر چه اساسی سرچ شود
    ordering = ('full_name',) #بر چه اساسی یوزر ها را مرتب کند
    filter_horizontal = () #دو تا مقدار را کنار هم نشان می دهد این به درد permision ها میخورد ولی چون ما نداریم خالی میزاریم


admin.site.unregister(Group)# گروپ ادمین پنل را حذف میکند
admin.site.register(User, UserAdmin)#ابتدا نام مدل مان سپس نام ادمین پنل