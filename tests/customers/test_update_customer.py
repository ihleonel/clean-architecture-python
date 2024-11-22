from unittest import TestCase
from unittest.mock import Mock
from src.customers.domain.customer import Customer
from src.customers.application.customer_updater import CustomerUpdater

class TestUpdateCustomer(TestCase):
    def setUp(self) -> None:
        self.customer_repository_mock = Mock()
        self.customer_updater = CustomerUpdater(self.customer_repository_mock)
        return super().setUp()

    def test_should_update_customer(self):
        expected_customer = Customer(1, "Leonel", "Ruiz Updated", "leonel.ruiz@gmail.com", "Av. Paulista, 1000")

        self.customer_repository_mock.find_by_id.return_value = Customer(1, "Leonel", "Ruiz", "leonel.ruiz@gmail.com", "Av. Paulista, 1000")
        self.customer_repository_mock.save.return_value = expected_customer

        customer = self.customer_updater.update(1, "Leonel", "Ruiz Updated", "leonel.ruiz@gmail.com", "Av. Paulista, 1000")

        self.customer_repository_mock.find_by_id.assert_called_once_with(1)
        self.customer_repository_mock.save.assert_called_once_with(expected_customer)
        self.assertEqual(expected_customer, customer)
