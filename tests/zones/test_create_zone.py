from unittest import TestCase
from src.zones.application.zone_creator import ZoneCreator
from src.commons.domain.validation_error import ValidationError
from tests.zones.fakers.zone_repository_faker import ZoneRepositoryFaker

class TestCreateZone(TestCase):
    def setUp(self):
        self.zone_repository = ZoneRepositoryFaker()
        self.zone_creator = ZoneCreator(self.zone_repository)
        return super().setUp()


    def test_create_zone(self):
        data = {
            'id': None,
            'name': 'Zone 1',
        }

        zone = self.zone_creator.create(data)

        self.assertEqual(data['id'], zone.id)
        self.assertEqual(data['name'], zone.name)

    def test_should_not_create_zone_if_name_is_empty(self):
        data = {
            'id': None,
            'name': '',
        }

        count = self.zone_repository.count()

        with self.assertRaises(ValidationError) as context:
            self.zone_creator.create(data)

        self.assertEqual('Name is required', context.exception.errors['name'])
        self.assertEqual(count, self.zone_repository.count())

