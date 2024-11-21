from src.customers.domain.customer import Customer
from src.customers.domain.customer_repository import CustomerRepository
from src.customers.domain.customer_validation import CustomerValidation

class CustomerCreator:
    def __init__(self, customer_respository: CustomerRepository) -> None:
        self.customer_repository = customer_respository
        self.customer_validation = CustomerValidation(self.customer_repository)
        pass

    def create(self, first_name: str, last_name: str, email: str, address: str) -> Customer:

        self.customer_validation.validate(first_name, last_name, email, address)

        customer = Customer(first_name, last_name, email, address)

        self.customer_repository.save(customer)

        return customer
