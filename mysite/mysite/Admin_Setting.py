from django.contrib.auth.models import User
user = User.objects.get(pk=1)
user = User.objects.get(username='15515255978')
user.set_password('lxw123456')
user.save()
