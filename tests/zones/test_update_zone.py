from unittest import TestCase
from src.zones.application.zone_updater import ZoneUpdater
from tests.zones.fakers.zone_repository_faker import ZoneRepositoryFaker

class TestUpdateZone(TestCase):
    def setUp(self):
        self.zone_repository = ZoneRepositoryFaker()
        self.zone_updater = ZoneUpdater(self.zone_repository)
        return super().setUp()

    def test_update_zone(self):
        data = {
            "id": "1",
            "name": "test update",
        }

        zone = self.zone_repository.find_by_id(data["id"])
        self.zone_repository.update(zone, data)

        self.zone_updater.update_zone(data)

        zone = self.zone_repository.find_by_id(data["id"])
        self.assertEqual(zone.name, data["name"])
