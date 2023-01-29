from typing import Optional
from uuid import UUID

from dtos.tree.baseTreeDTO import BaseTreeDTO


class PatchTreeRootDTO(BaseTreeDTO):
    isConfidential: Optional[bool]
    prevAncestor: Optional[UUID]
    nextAncestor: Optional[UUID]
