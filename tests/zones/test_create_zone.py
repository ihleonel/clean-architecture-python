from unittest import TestCase
from src.zones.application.zone_creator import ZoneCreator
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

