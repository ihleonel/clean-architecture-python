from src.users.domain.user_repository import UserRepository
from src.users.domain.user_typed_dict import UserTypedDict


class UserCreator:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, data: UserTypedDict) -> UserTypedDict:
        if self.user_repository.email_already_exists(data["email"]):
            raise ValueError("Email already exists")
        user = self.user_repository.save(data)
        return user
