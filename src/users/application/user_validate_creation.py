from src.users.domain.user_repository import UserRepository
from src.commons.domain.result import Result, Error, Success


class UserValidateCreation:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def validate(self, name: str, email: str, password: str) -> Result[None]:
        errors: dict[str, list[str]] = {}

        name_result = self.validate_name(name)
        if isinstance(name_result, Error):
            errors.update(name_result.errors)

        email_result = self.validate_email(email)
        if isinstance(email_result, Error):
            errors.update(email_result.errors)

        password_result = self.validate_password(password)
        if isinstance(password_result, Error):
            errors.update(password_result.errors)

        if errors:
            return Error(errors)
        return Success(None)

    def validate_name(self, name: str) -> Result[None]:
        if not name:
            return Error({"name": ["Name is required"]})
        return Success(None)

    def validate_email(self, email: str) -> Result[None]:
        if not email:
            return Error({"email": ["Email is required"]})
        elif self.user_repository.email_already_exists(email):
            return Error({"email": ["Email already exists"]})
        return Success(None)

    def validate_password(self, password: str) -> Result[None]:
        if not password:
            return Error({"password": ["Password is required"]})
        elif len(password) < 8:
            return Error({"password": ["Password must be at least 8 characters long"]})
        elif not any(char.isdigit() for char in password):
            return Error({"password": ["Password must contain at least one digit"]})
        return Success(None)
