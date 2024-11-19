from src.customers.domain.customer import Customer
from src.customers.domain.customer_repository import CustomerRepository

class CustomerCreator:
    def __init__(self, customer_respository: CustomerRepository) -> None:
        self.customer_repository = customer_respository
        pass

    def create(self, first_name: str, last_name: str, email: str, address: str) -> None:
        customer = Customer(first_name, last_name, email, address)
        self.customer_repository.save(customer)
