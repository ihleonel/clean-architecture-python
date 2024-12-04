from src.routes.domain.route import Route
from src.routes.domain.route_repository import RouteRepository

class RouteRepositoryFaker(RouteRepository):
    def __init__(self) -> None:
        self.routes = []

    def save(self, route: Route) -> None:
        self.routes.append(route)

    def name_already_exists(self, name: str) -> bool:
        return name in [route.name for route in self.routes]

    def count(self) -> int:
        return len(self.routes)
