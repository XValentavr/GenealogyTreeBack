from django.core.exceptions import ValidationError
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from deal.models import DealWithClient
from userprofile.models import UserProfile
from deal.serializers import DealSerializers, CreateDealSerializer, UpdatePartialDealSerializer


# Create your views here.


class DealClientView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request, uuid):
        """
        this function creates GET request to get info about user profile
        :param request: all request data (body, headers)
        :param uuid: user unique identifier
        :return: json object from got data
        """
        client = DealWithClient.objects.select_related('client').filter(client__user__uid=uuid,
                                                                        is_published=request.data['is_published'])
        serializer = DealSerializers(client, many=True, context={"request": request})
        if serializer:
            return Response(serializer.data, status=HTTP_200_OK)
        return Response('Nothing to show', status=404)

    @staticmethod
    def post(request, uuid):
        """
        Create new deal
        :param request: all request data (body, headers)
        :param uuid: user unique udentifier
        :return: json object from got data
        """
        request.data['client'] = UserProfile.objects.select_related('user').filter(user__uid=uuid).first().id
        deal = CreateDealSerializer(data=request.data)
        if deal.is_valid():
            deal.save()
            return Response("It's OK.", status=HTTP_200_OK)
        return Response(status=500)


class DealClientChangeView(APIView):
    """
    This class cat change (delete and patch) deal
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def patch(request, uuid, unique):
        """
        Create patch request
        :param request: all request data (body, headers)
        :param uuid: user unique udentifier
        :param unique: deal identifier
        :return: status of transaction
        """
        # can be updated

        client = UserProfile.objects.select_related('user').filter(user__uid=uuid).first()
        deal = DealWithClient.objects.filter(client_id=client.id, unique=unique).first()
        deal = UpdatePartialDealSerializer(deal, data=request.data, partial=True)
        if deal.is_valid(raise_exception=True):
            deal.save()
            return Response("It's OK.", status=HTTP_200_OK)
        return Response('Deal not found.', status=500)

    @staticmethod
    def delete(request, uuid, unique):
        """
        Create delete request
        :param request: all request data (body, headers)
        :param uuid: user unique udentifier
        :param unique: deal identifier
        :return: status of transaction
        """
        try:
            client = UserProfile.objects.select_related('user').filter(user__uid=uuid).first()
            DealWithClient.objects.filter(client_id=client.id, unique=unique).delete()

            return Response("Deal has been deleted.", status=HTTP_200_OK)
        except ValidationError:
            return Response('Deal not found.', status=500)
