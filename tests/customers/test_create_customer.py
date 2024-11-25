from unittest import TestCase
from unittest.mock import Mock
from src.customers.domain.customer import Customer
from src.customers.application.customer_creator import CustomerCreator
from src.commons.domain.validation_error import ValidationError

class TestCreateCustomer(TestCase):
    def setUp(self) -> None:
        self.customer_repository_mock = Mock()
        self.customer_creator = CustomerCreator(self.customer_repository_mock)
        return super().setUp()


    def test_should_create_customer(self):
        self.customer_repository_mock.email_already_exists.return_value = False

        data = {
            "id": None,
            "first_name": "Leonel",
            "last_name": "Ruiz",
            "email": "leonel.ruiz@gmail.com",
            "address": "Av. Paulista, 1000"
        }
        customer = self.customer_creator.create(data=data)
        self.customer_repository_mock.save.assert_called_once_with(customer)
        self.customer_repository_mock.email_already_exists.assert_called_once_with("leonel.ruiz@gmail.com")


    def test_should_not_create_customer_with_invalid_data(self):
        data = {
            "id": None,
            "first_name": "",
            "last_name": "Ruiz",
            "email": "",
            "address": "Av. Paulista, 1000"
        }
        with self.assertRaises(ValidationError) as context:
            self.customer_creator.create(data=data)

        self.assertEqual("First name is required", context.exception.errors["first_name"])
        self.assertEqual("Email is required", context.exception.errors["email"])


    def test_should_not_create_customer_with_duplicated_email(self):
        self.customer_repository_mock.email_already_exists.return_value = True
        data = {
            "id": None,
            "first_name": "Leonel",
            "last_name": "Ruiz",
            "email": "leonel.ruiz@gmail.com",
            "address": "Av. Paulista, 1000"
        }

        with self.assertRaises(ValidationError) as context:
            self.customer_creator.create(data=data)

        self.assertEqual("Email already exists", context.exception.errors["email"])
