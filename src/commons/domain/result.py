from dataclasses import dataclass
from typing import TypeVar, Union, Generic


T = TypeVar("T")

@dataclass(frozen=True)
class Error:
    errors: dict[str, list[str]]

@dataclass(frozen=True)
class Success(Generic[T]):
    value: T

Result = Union[Success[T], Error]
