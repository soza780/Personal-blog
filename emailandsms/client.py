from django.contrib.auth.models import User

queryset = User.objects.all()

print(queryset)
