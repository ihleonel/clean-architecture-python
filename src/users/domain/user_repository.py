
from abc import ABC, abstractmethod

from src.users.domain.user_typed_dict import UserTypedDict


class UserRepository(ABC):
    @abstractmethod
    def save(self, data: UserTypedDict) -> UserTypedDict:
        pass

    @abstractmethod
    def email_already_exists(self, email: str) -> bool:
        pass
