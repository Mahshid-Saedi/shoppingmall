from django.shortcuts import render
from django.views import View
from .forms import UserRegisterationForm

class UserRegisterView(View):
    from_class = UserRegisterationForm
    def get(self, request):#نمایش فرم به کاربر
        form = self.from_class
        return render(request, 'account/register.html', {'form':form})


    def post(self, request):
        pass

