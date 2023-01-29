import uuid

from authentication.models import UserAccount
from tree.models import MainRootUser


def add_new_params_to_request(request, myuuid):
    """
    Adds specific data to request
    :param request: request to add new data
    :param myuuid: unique identifier
    :return: changed requests
    """
    if 'wife' in request.data:
        request.data['wife'] = None
        request.data['spouse'] = MainRootUser.objects.filter(user__uid=myuuid).first().pk

    elif 'spouse' in request.data:
        request.data['spouse'] = None
        request.data['wife'] = MainRootUser.objects.filter(user__uid=myuuid).first().pk

    if 'email' in request.data:
        user = UserAccount.objects.filter(email=request.data['email'])
        for usr in user:
            if usr.uid == uuid.UUID(myuuid):
                request.data['is_you'] = True
                return request
            if not usr:
                usr = ''
            request.data['user'] = usr.pk
    return request
