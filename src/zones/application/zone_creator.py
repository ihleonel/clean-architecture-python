from src.zones.domain.zone import Zone
from src.zones.domain.zone_create_validator import ZoneCreateValidator

class ZoneCreator:
    def __init__(self, zone_repository) -> None:
        self.zone_repository = zone_repository
        self.zone_validator = ZoneCreateValidator(zone_repository)

    def create(self, data: dict) -> Zone:
        self.zone_validator.validate(data)

        zone = Zone(**data)

        self.zone_repository.save(zone)

        return zone
