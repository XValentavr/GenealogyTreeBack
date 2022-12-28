from django.core.mail import send_mail
from rest_framework import authentication, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from support.serializer import TechSupportSerializer


# Create your views here.


class CreateTechSupportMessage(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TechSupportSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        send_mail(subject='Питання з генеологічного сайту',
                  message=self.request.data['context'] + '\n\n' +
                          self.request.data['phone'] + '\n\n\n' +
                          self.request.data['name'] + '\n' +
                          self.request.data['date'],
                  from_email=self.request.data['email'],
                  recipient_list=['iwilly17@gmail.com'],
                  fail_silently=False,
                  )
        return Response({
            'status': 200
        })
