from unittest import TestCase
from src.commons.domain.validation_error import ValidationError
from src.routes.domain.route_repository import RouteRepository
from src.routes.application.route_creator import RouteCreator
from tests.routes.fakers.route_repository_faker import RouteRepositoryFaker

class TestCreateRoute(TestCase):
    route_repository: RouteRepository
    route_creator: RouteCreator

    def setUp(self):
        self.route_repository = RouteRepositoryFaker()
        self.route_creator = RouteCreator(self.route_repository)
        return super().setUp()

    def test_create_route(self):
        data = {
            'id': None,
            'name': 'test',
        }
        count = self.route_repository.count()

        route = self.route_creator.create(data)

        self.assertEqual(route.name, data['name'])
        self.assertEqual(count + 1, self.route_repository.count())

    def test_should_not_create_route_with_invalid_data(self):
        data = {
            'id': None,
            'name': '',
        }

        count = self.route_repository.count()

        with self.assertRaises(ValidationError) as context:
            self.route_creator.create(data)

        self.assertEqual(context.exception.errors, {'name': 'Name is required'})
        self.assertEqual(count, self.route_repository.count())
