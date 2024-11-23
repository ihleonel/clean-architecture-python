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
        old_customer = Customer(1, "Leonel", "Ruiz ", "leonel.ruiz@gmail.com", "Av. Paulista, 1000")
        self.customer_repository_mock.find_by_id.return_value = old_customer

        new_customer = self.customer_updater.update(1, "Leonel", "Ruiz Updated", "leonel.ruiz.updated@gmail.com", "Av. Paulista, 1000")

        self.assertEqual(new_customer.first_name, "Leonel")
        self.assertEqual(new_customer.last_name, "Ruiz Updated")
        self.assertEqual(new_customer.email, "leonel.ruiz.updated@gmail.com")
