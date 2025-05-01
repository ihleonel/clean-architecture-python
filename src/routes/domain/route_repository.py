from abc import ABC, abstractmethod
from src.routes.domain.route import Route

class RouteRepository(ABC):
    @abstractmethod
    def save(self, route: Route) -> None: ...

    @abstractmethod
    def name_already_exists(self, name: str) -> bool: ...

    @abstractmethod
    def count(self) -> int: ...
