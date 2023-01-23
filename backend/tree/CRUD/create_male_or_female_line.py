from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from tree.models import MainRootUser, MaleLine


def create_male_of_female_line(uuid, lineInfo, model):
    treeRootUser = MainRootUser.objects.filter(rootUser__id=uuid).first()
    if lineInfo.is_valid():
        lineInfo.save()
        model.objects.create(anyInfo_id=lineInfo.data['id'], prevAncestor_id=None,
                             root_id=treeRootUser.id)
        return Response(status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)
