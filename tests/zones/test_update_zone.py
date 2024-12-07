from unittest import TestCase
from src.zones.application.zone_updater import ZoneUpdater
from tests.zones.fakers.zone_repository_faker import ZoneRepositoryFaker

class TestUpdateZone(TestCase):
    def setUp(self):
        self.zone_repository = ZoneRepositoryFaker()
        self.zone_updater = ZoneUpdater(self.zone_repository)
        return super().setUp()

    def test_update_zone(self):
        pass
