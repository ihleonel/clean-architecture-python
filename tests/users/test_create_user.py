from unittest import TestCase
from unittest.mock import Mock
from src.users.domain.user_typed_dict import UserTypedDict
from src.users.application.user_creator import UserCreator

class TestCreateUser(TestCase):
    def setUp(self) -> None:
        self.user_repository_mock = Mock()
        self.user_creator = UserCreator(self.user_repository_mock)
        return super().setUp()

    def test_should_create_user(self):
        data: UserTypedDict = {
            "id": 1,
            "name": "Juan Ruiz",
            "email": "juan.ruiz@example.com",
            "password": "password123"
        }

        self.user_repository_mock.email_already_exists.return_value = False
        self.user_creator.create(data=data)
        self.user_repository_mock.save.assert_called_once_with(data)
        self.user_repository_mock.email_already_exists.assert_called_once_with("juan.ruiz@example.com")

    def test_should_not_create_user_with_invalid_data(self):
        pass


    def test_should_not_create_user_with_duplicated_email(self):
        pass
