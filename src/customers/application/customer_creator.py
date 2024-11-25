from src.customers.domain.customer import Customer
from src.customers.domain.customer_repository import CustomerRepository
from src.customers.domain.customer_create_validation import CustomerCreateValidation

class CustomerCreator:
    def __init__(self, customer_respository: CustomerRepository) -> None:
        self.customer_repository = customer_respository
        self.customer_create_validation = CustomerCreateValidation(self.customer_repository)


    def create(self, data: dict) -> Customer:

        self.customer_create_validation.validate(data)

        customer = Customer(**data)

        self.customer_repository.save(customer)

        return customer
