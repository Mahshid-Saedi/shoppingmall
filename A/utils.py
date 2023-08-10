# در این فایل متد هایی که در همه جا به درد می خورد را می نویسیم
#این تابع شماره تلفن و یک کد را میگیرد که به یک سرویس دهنده خارجی وصل میشود و اسمس را میفرستد


from kavenegar import *

def send_otp_code(phone_number, code):
    pass

    try:
        api = KavenegarAPI('49376943337435456B47452F59416553656E6B527338356F566268337A58312B2B545164636237744373453D')
        params = {
            'sender': '',#optional
            'receptor': phone_number,#multiple mobile number, split by comma
            'message': f'{code}کد تایید شما',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
        
