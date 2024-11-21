from abc import ABC, abstractmethod
from src.customers.domain.customer import Customer

class CustomerRepository(ABC):
    @abstractmethod
    def save(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Customer|None:
        pass

    @abstractmethod
    def email_already_exists(self, email: str) -> bool:
        pass
