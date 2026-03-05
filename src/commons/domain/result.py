from dataclasses import dataclass
from typing import TypeVar, Union, Generic


T = TypeVar("T")
E = TypeVar("E")

@dataclass(frozen=True)
class Error(Generic[E]):
    errors: list[E]

@dataclass(frozen=True)
class Success(Generic[T]):
    value: T

Result = Union[Success[T], Error[E]]
