from src.customers.domain.customer import Customer
from src.customers.domain.customer_repository import CustomerRepository
from src.customers.domain.customer_update_validation import CustomerUpdateValidation

class CustomerUpdater:
    def __init__(self, customer_repository: CustomerRepository) -> None:
        self.customer_repository = customer_repository

    def update(self, data: dict) -> Customer:
        customer_update_validation = CustomerUpdateValidation(self.customer_repository)
        customer_update_validation.validate(data=data)

        customer = self.customer_repository.find_by_id(data["id"])
        customer.first_name = data["first_name"]
        customer.last_name = data["last_name"]
        customer.email = data["email"]
        customer.address = data["address"]

        self.customer_repository.save(customer)

        return customer
