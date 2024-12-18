from src.zones.domain.zone import Zone
from src.zones.domain.zone_update_validator import ZoneUpdateValidator

class ZoneUpdater:
    def __init__(self, zone_repository):
        self.zone_repository = zone_repository
        self.zone_update_validator = ZoneUpdateValidator(zone_repository=self.zone_repository)

    def update(self, data: dict) -> Zone:

        self.zone_update_validator.validate(data)

        zone = self.zone_repository.find_by_id(data["id"])

        self.zone_repository.update(zone, data)
        return zone
