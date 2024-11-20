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
        expected_customer = Customer("Leonel", "Ruiz", "leonel.ruiz@gmail.com", "Av. Paulista, 1000")
        self.customer_repository_mock.find_by_email.return_value = expected_customer
        self.customer_repository_mock.count.return_value = 1

        self.customer_creator.create("Leonel", "Ruiz", "leonel.ruiz@gmail.com", "Av. Paulista, 1000")

        customer = self.customer_repository_mock.find_by_email("leonel.ruiz@gmail.com")

        self.assertEqual(1, self.customer_repository_mock.count())
        self.assertEqual("Leonel", customer.first_name)
        self.assertEqual("Ruiz", customer.last_name)
        self.assertEqual("leonel.ruiz@gmail.com", customer.email)
        self.assertEqual("Av. Paulista, 1000", customer.address)

    def test_should_not_create_customer_when_email_already_exists(self):
        with self.assertRaises(ValidationError) as context:
            self.customer_creator.create("", "Ruiz", "", "Av. Paulista, 1000")

        self.assertEqual("First name is required", context.exception.errors["first_name"])
        self.assertEqual("Email is required", context.exception.errors["email"])
