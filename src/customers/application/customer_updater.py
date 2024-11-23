from src.customers.domain.customer import Customer
from src.customers.domain.customer_repository import CustomerRepository

class CustomerUpdater:
    def __init__(self, customer_repository: CustomerRepository) -> None:
        self.customer_repository = customer_repository

    def update(self, id: int, first_name: str, last_name: str, email: str, address: str) -> Customer:
        # customer_update_validation = CustomerUpdateValidation(self.customer_repository)
        # customer_update_validation.validate(id, first_name, last_name, email, address)

        customer = self.customer_repository.find_by_id(id)

        customer.first_name = first_name
        customer.last_name = last_name
        customer.email = email
        customer.address = address

        self.customer_repository.save(customer)

        return customer
