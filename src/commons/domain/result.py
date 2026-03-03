from dataclasses import dataclass
from typing import TypeVar, Union, Generic


T = TypeVar("T")

@dataclass(frozen=True)
class Error:
    errors: dict[str, list[str]]

    def __init__(self, errors: dict[str, list[str]]) -> None:
        for key, error in errors.items():
            if key in self.errors:
                self.errors[key].extend(error)
            else:
                self.errors[key] = error

@dataclass(frozen=True)
class Success(Generic[T]):
    value: T

Result = Union[Success[T], Error]
