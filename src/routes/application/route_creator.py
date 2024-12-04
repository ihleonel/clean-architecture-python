from src.routes.domain.route import Route
from src.routes.domain.route_repository import RouteRepository
from src.routes.domain.route_create_validation import RouteCreateValidation

class RouteCreator:
    def __init__(self, route_repository: RouteRepository) -> None:
        self.route_repository = route_repository
        self.route_create_validation = RouteCreateValidation(self.route_repository)

    def create(self, data: dict) -> Route:
        self.route_create_validation.validate(data)

        route = Route(**data)

        self.route_repository.save(route)

        return route

