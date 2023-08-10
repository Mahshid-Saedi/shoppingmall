from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

  #در اینجا url های مربوط به هرapp مان را می نویسیم
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls', namespace = 'home')),
    path('account/', include('account.urls', namespace = 'account')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # اما باید مراقب باشیم زمان اجرا ی برنامه در محیط واقعی باید این را پاک کنیم
