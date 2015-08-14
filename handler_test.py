#-*-encoding:utf-8-*-
import smshandler.handler as handler


user_data = {"phone":"79123456789","message":"Hello!"}

sms_handler1 = handler.get_handler_by_name("smsc")
sms_handler1.send(**user_data)

sms_handler2 = handler.get_handler_by_name("sms-traffic")
sms_handler2.send(**user_data)

sms_handler3 = handler.get_handler("http://somegate.ru/api/message/", 
	                               login = "asd", password = "qwerty123")
sms_handler3.send(**user_data)

