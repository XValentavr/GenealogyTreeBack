from tree.models import AnyTreeInfo


def create_initial_any_info(treeRootUser, treeRootUserAnyInfo):
    if not treeRootUserAnyInfo:
        anyInfo = AnyTreeInfo.objects.create(firstName=None, surname=None, lastName=None, motherSurname=None,
                                             dateOfBirth=None, placeOfBirth=None, dateOfMarry=None,
                                             dateOfDeath=None, placeOfDeath=None, reasonOfDeath=None, document=None,
                                             isPublished=False, sex='м',
                                             isConfidential=False)

        treeRootUser.anyInfo = anyInfo
        treeRootUser.save()
        return anyInfo
