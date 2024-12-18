
from src.zones.domain.zone_repository import ZoneRepository
from src.zones.domain.zone_create_validator import ZoneCreateValidator

class ZoneUpdateValidator(ZoneCreateValidator):
    def __init__(self, zone_repository: ZoneRepository):
        super().__init__(zone_repository)

    def validate_id(self, id: int) -> None:
        if not id:
            self.errors["id"] = "Id is required"
        elif self.zone_repository.find_by_id(id) is None:
            self.errors["id"] = "Zone not found"
