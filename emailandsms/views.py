import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

import djangoProject.settings
from .forms import SmsForm


# Create your views here.

@login_required
def send_sms_view(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            form = SmsForm(request.POST)
            if form.is_valid():
                receptor = form.cleaned_data['receptor']
                message = form.cleaned_data['message']
                if receptor == 'ALL':
                    receptor = ''
                    queryset = User.objects.all()
                    for _i in queryset:
                        receptor += _i.phone_number
                        receptor += ','
                url = djangoProject.settings.API_KEY
                payload = {'receptor': receptor, 'message': message}
                answer = requests.post(url=url, data=payload)
    else:
        form = SmsForm()
        answer = 'message did not sent'

    context = {
        'form': form,
        'answer': answer,
    }
    return render(request, 'emailandsms/sms.html', context)


def send_email_view(request):
    pass
