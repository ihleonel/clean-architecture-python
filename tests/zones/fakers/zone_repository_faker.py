from src.zones.domain.zone_repository import ZoneRepository
from src.zones.domain.zone import Zone

class ZoneRepositoryFaker(ZoneRepository):
    def __init__(self) -> None:
        self.zones = [
            Zone(id=1, name="Zone 1000"),
        ]

    def save(self, zone: Zone) -> None:
        self.zones.append(zone)

    def name_already_exists(self, name: str) -> bool:
        for zone in self.zones:
            if zone.name == name:
                return True
        return False
