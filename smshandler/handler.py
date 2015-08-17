#-*-encoding:utf-8-*-
from .models import HandlerLog
from django.conf import settings
import urllib2
from django.utils.http import urlencode
import simplejson as json

class WrongHandlerName(NameError):
    def __init__(self, handler_name):
        self.msg = "Hander with name %s does not exists."%handler_name

class SMSHandler(object):
    '''
    Base Handler class.
    Every handler must have send method implementation;
    Every handler must have SMS centre address.
    If login or password is None then send request to sms centre without this parameters.
    Settings:
        SMS_GATES = {
            "<handler_name>":{
                "address":"<address>",
            },
            "<handler_name>":{
                "address":"<address>",
                "login":"<login>",
                "password":"<password>",
            },
            "<handler_name>":{
                "address":"<address>",
                "login":"<login>",
                "password":"<password>",
                "field_names":{
                    "login_field_name":"<login_field_name>",
                    "password_field_name":"<password_field_name>",
                     ...
                }
            },
        }
    '''

    def __init__(self, handler_address, login = None, password = None, **kwargs):
        super(SMSHandler, self).__init__()
        self.handler_address = handler_address
        self.login = login
        self.password = password
        self.login_field_name = kwargs.get('login_field_name','login')
        self.password_field_name = kwargs.get('password_field_name','psw')
        self.phone_field_name = kwargs.get('phone_field_name','phone')
        self.message_field_name = kwargs.get('message_field_name','message')
        self.status_field_name = kwargs.get('status_field_name','status')
        self.error_code_field_name = kwargs.get('error_code_field_name','error_code')
        self.error_msg_field_name = kwargs.get('error_msg_field_name','error_msg')

    def _write_log(self, status, phone, error_code = None, error_msg = None):
        hl = HandlerLog(status = status, phone = phone, error_code = error_code,
                                                             error_msg = error_msg)
        hl.save()

    def send(self, phone, message, **kwargs):
        data = kwargs
        data[self.phone_field_name] = phone
        data[self.message_field_name] = message
        if self.login is not None and self.password is not None:
            data[self.login_field_name] = self.login
            data[self.password_field_name] = self.password
        result = urllib2.urlopen(self.handler_address, urlencode(list(data.items())))
        message_status = json.load(result)
        self._write_log(
            message_status[self.status_field_name], 
            message_status[self.phone_field_name],
            message_status.get(self.error_code_field_name, None),
            message_status.get(self.msg_code_field_name, None)
        )
        return message_status

def get_handler_by_name(handler_name):
    '''
    Use it for getting handlers that was defined in settings.SMS_GATES
    '''
    if hasattr(settings,"SMS_GATES"):
        if settings.SMS_GATES.has_key(handler_name):
            handler_settings = settings.SMS_GATES[handler_name]
            return SMSHandler(handler_settings["address"],
                handler_settings.get("login", None),
                handler_settings.get("password", None),
                **handler_settings.get("field_names",{})
            )
    raise WrongHandlerName(handler_name)

def get_handler(address, login = None, password = None, **kwargs):
    '''
    Use it for creating your handlers right in code.
    '''
    return SMSHandler(
            address,
            login,
            password,
            **kwargs
        )
