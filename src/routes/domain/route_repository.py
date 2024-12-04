from abc import ABC, abstractmethod
from src.routes.domain.route import Route

class RouteRepository(ABC):
    @abstractmethod
    def save(self, route: Route) -> None:
        pass

    @abstractmethod
    def name_already_exists(self, name: str) -> bool:
        pass

    @abstractmethod
    def count(self) -> int:
        pass
