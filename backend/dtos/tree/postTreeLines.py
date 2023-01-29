from typing import Optional

from dtos.tree.baseTreeDTO import BaseTreeDTO


class PostTreeLineDTO(BaseTreeDTO):
    isConfidential: Optional[bool]
