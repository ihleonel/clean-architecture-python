from src.customers.domain.customer import Customer

class CustomerUpdater:
    def __init__(self, customer_repository) -> None:
        self.customer_repository = customer_repository

    def update(self, id: int, first_name: str, last_name: str, email: str, address: str) -> Customer:
        customer = self.customer_repository.find_by_id(id)
        customer.update(first_name, last_name, email, address)

        return self.customer_repository.save(customer)
