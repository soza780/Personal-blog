from django.urls import path

from .views import send_email_view, send_sms_view

app_name = 'mail'

urlpatterns = [
    path('email/', send_email_view, name='email_view'),
    path('sms/', send_sms_view, name='sms_view'),

]
