from celery import shared_task
from account.models import OtpCode
from datetime import datetime, timedelta
import pytz

@shared_task()
def remove_expired_otp_code():#این تابع کد های منقضی شده را حذف میکند
    expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    OtpCode.objects.filter(created__lt=expired_time).delete()