from src.routes.domain.route_repository import RouteRepository
from src.commons.domain.validation_error import ValidationError

class RouteCreateValidation:
    route_repository: RouteRepository
    errors: dict

    def __init__(self, route_repository: RouteRepository) -> None:
        self.route_repository = route_repository
        self.errors = {}

    def validate(self, data: dict) -> None:
        self.validate_name(data['name'])

        if len(self.errors) > 0:
            raise ValidationError(self.errors)

    def validate_name(self, name: str) -> None:
        if name is None or name == '':
            self.errors['name'] = 'Name is required'
        elif self.route_repository.name_already_exists(name) is True:
            self.errors['name'] = 'Name already exists'

