from src.commons.domain.validation_error import ValidationError
from src.customers.domain.customer_repository import CustomerRepository

class CustomerCreateValidation:
    def __init__(self, document_repository: CustomerRepository) -> None:
        self.document_repository = document_repository
        self.errors = {}

    def validate(self, data: dict) -> None:
        self.validate_id(data["id"])
        self.validate_first_name(data["first_name"])
        self.validate_last_name(data["last_name"])
        self.validate_email(data["email"])
        self.validate_address(data["address"])

        if len(self.errors) > 0:
            raise ValidationError(self.errors)

    def validate_id(self, id: int) -> None:
        if not id is None:
            self.errors["id"] = "Id should be null"

    def validate_first_name(self, first_name: str) -> None:
        if first_name is None or first_name == "":
            self.errors["first_name"] = "First name is required"

    def validate_last_name(self, last_name: str) -> None:
        if last_name is None or last_name == "":
            self.errors["last_name"] = "Last name is required"

    def validate_email(self, email: str) -> None:
        if email is None or email == "":
            self.errors["email"] = "Email is required"
        elif self.document_repository.email_already_exists(email) is True:
            self.errors["email"] = "Email already exists"

    def validate_address(self, address: str) -> None:
        if address is None or address == "":
            self.errors["address"] = "Address is required"


