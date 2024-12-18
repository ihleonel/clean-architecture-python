from src.commons.domain.validation_error import ValidationError
from src.zones.application.zone_updater import ZoneUpdater
from tests.zones.fakers.zone_repository_faker import ZoneRepositoryFaker
from unittest import TestCase

class TestUpdateZone(TestCase):
    def setUp(self):
        self.zone_repository = ZoneRepositoryFaker()
        self.zone_updater = ZoneUpdater(self.zone_repository)
        return super().setUp()

    def test_update_zone(self):
        data = {
            "id": 1,
            "name": "test update",
        }

        self.zone_updater.update(data)

        zone = self.zone_repository.find_by_id(data["id"])
        self.assertEqual(zone.name, data["name"])

    def test_should_not_update_zone_if_id_is_not_found(self):
        data = {
            "id": 1001,
            "name": "test update",
        }

        with self.assertRaises(ValidationError) as context:
            self.zone_updater.update(data)

        self.assertEqual("Zone not found", context.exception.errors["id"])

    def test_should_not_update_zone_if_name_is_empty(self):
        data = {
            "id": 1,
            "name": "",
        }

        with self.assertRaises(ValidationError) as context:
            self.zone_updater.update(data)

        self.assertEqual("Name is required", context.exception.errors["name"])

    def test_should_not_update_zone_if_name_already_exists(self):
        data = {
            "id": 1,
            "name": "Zone 1000",
        }

        with self.assertRaises(ValidationError) as context:
            self.zone_updater.update(data)

        self.assertEqual("Name already exists", context.exception.errors["name"])
