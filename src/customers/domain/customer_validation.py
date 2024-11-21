from src.commons.domain.validation_error import ValidationError
from src.customers.domain.customer_repository import CustomerRepository

class CustomerValidation:
    def __init__(self, document_repository: CustomerRepository) -> None:
        self.document_repository = document_repository

    def validate(self, first_name: str, last_name: str, email: str, address: str) -> None:
        errors = {}

        if first_name is None or first_name == "":
            errors["first_name"] = "First name is required"

        if last_name is None or last_name == "":
            errors["last_name"] = "Last name is required"

        if email is None or email == "":
            errors["email"] = "Email is required"
        elif self.document_repository.email_already_exists(email) is True:
            errors["email"] = "Email already exists"

        if address is None or address == "":
            errors["address"] = "Address is required"

        if len(errors) > 0:
            raise ValidationError(errors)
