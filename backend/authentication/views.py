from django.views.generic import TemplateView


# Create your views here.

class RegisterView(TemplateView):
    template_name = 'authentication/base.html'


class ResetPassword(TemplateView):
    template_name = 'authentication/reset_password.html'


class SetNewPassword(TemplateView):
    template_name = 'authentication/set_new_password.html'
