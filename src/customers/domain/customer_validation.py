from src.commons.domain.validation_error import ValidationError

class CustomerValidation:
    def validate(self, first_name: str, last_name: str, email: str, address: str) -> None:
        errors = {}
        if first_name is None or first_name == "":
            errors["first_name"] = "First name is required"

        if last_name is None or last_name == "":
            errors["last_name"] = "Last name is required"

        if email is None or email == "":
            errors["email"] = "Email is required"

        if address is None or address == "":
            errors["address"] = "Address is required"

        if len(errors) > 0:
            raise ValidationError(errors)
