from dataclasses import dataclass
from typing import Any, Optional

from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.PASCAL)
@dataclass
class Response:
    """Class that represents default BAS response."""

    success: bool = False
    """[description]"""

    message: Optional[str] = None
    """Response error message."""

    result: Any = None
    """Response result object."""


__all__ = ["Response"]
