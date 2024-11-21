from dataclasses import dataclass

@dataclass
class Customer:
    first_name: str
    last_name: str
    email: str
    address: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
