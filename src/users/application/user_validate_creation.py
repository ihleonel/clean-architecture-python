from src.users.domain.user_repository import UserRepository
from src.commons.domain.result import Result as Validation, Error, Success


class UserValidateCreation:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate(self, name: str, email: str, password: str) -> Validation[None, dict[str, list[str]]]:
        errors: dict[str, list[str]] = {}

        name_result = self.validate_name(name)
        if name_result:
            errors.update(name_result)

        email_result = self.validate_email(email)
        if email_result:
            errors.update(email_result)

        password_result = self.validate_password(password)
        if password_result:
            errors.update(password_result)

        if errors:
            return Error(errors)
        return Success(None)

    def validate_name(self, name: str) -> dict[str, list[str]] | None:
        errors: list[str] = []
        if not name:
            errors.append("Name is required")
        elif len(name) < 3:
            errors.append("Name must be at least 3 characters long")
        if errors:
            return {"name": errors}
        return None

    def validate_email(self, email: str) -> dict[str, list[str]] | None:
        errors: list[str] = []
        if not email:
            errors.append("Email is required")
        elif self.user_repository.email_already_exists(email):
            errors.append("Email already exists")
        if errors:
            return {"email": errors}
        return None

    def validate_password(self, password: str) -> dict[str, list[str]] | None:
        errors: list[str] = []
        if not password:
            errors.append("Password is required")

        if len(password) < 8:
            errors.append("Password must be at least 8 characters long")

        if not any(char.isdigit() for char in password):
            errors.append("Password must contain at least one digit")

        if errors:
            return {"password": errors}
        return None
