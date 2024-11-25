from src.customers.domain.customer_create_validation import CustomerCreateValidation

class CustomerUpdateValidation(CustomerCreateValidation):
    def validate_id(self, id: int) -> None:
        if id is None:
            self.errors["id"] = "Id is required"
        elif self.document_repository.find_by_id(id) is None:
            self.errors["id"] = "Id does not exist"


    def validate_email(self, email: str) -> None:
        if email is None or email == "":
            self.errors["email"] = "Email is required"
        elif self.document_repository.email_already_exists(email) is True:
            self.errors["email"] = "Email already exists"
