from django.db import models

class HandlerLog(models.Model):
    '''
    SMS handler logs.
    status is True when message sent with success in other cases is False.
    '''
    status = models.BooleanField(max_length=10, verbose_name=u'Status')
    phone = models.CharField(verbose_name=u'Phone', max_length=13)
    error_code = models.IntegerField(verbose_name = "Error code", null=True)
    error_msg = models.CharField(verbose_name='Error message', max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = "Handler log"
        verbose_name_plural = "Handler logs"

    def __str__(self):
        return "%s %s"%(phone,
            "SUCCESS" if status else "FAIL")
