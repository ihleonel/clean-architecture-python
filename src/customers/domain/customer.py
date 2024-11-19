class Customer:
    def __init__(self, first_name: str, last_name: str, email: str, address: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
