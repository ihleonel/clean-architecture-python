from src.users.domain.user_repository import UserRepository
from src.users.domain.user_typed_dict import UserTypedDict
from src.users.application.user_validate_creation import UserValidateCreation
from src.commons.domain.result import Result, Error, Success

class UserCreator:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.user_validate_creation = UserValidateCreation(user_repository)

    def create(self, data: UserTypedDict) -> Result[UserTypedDict]:
        validation_result: Result[None] = self.user_validate_creation.validate(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )

        if isinstance(validation_result, Error):
            return validation_result

        user = self.user_repository.save(data)
        return Success(user)
