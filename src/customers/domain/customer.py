from dataclasses import dataclass

@dataclass(frozen=True)
class Customer:
    id: int|None
    first_name: str
    last_name: str
    email: str
    address: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
