from src.zones.domain.zone_repository import ZoneRepository
from src.zones.domain.zone import Zone

class ZoneRepositoryFaker(ZoneRepository):
    def __init__(self) -> None:
        self.zones = [
            Zone(id=1, name="Zone 1000"),
        ]

    def save(self, zone: Zone) -> None:
        self.zones.append(zone)

    def update(self, zone: Zone) -> None:
        for item in self.zones:
            if zone.id == item.id:
                item = zone
                return

    def name_already_exists(self, name: str) -> bool:
        for zone in self.zones:
            if zone.name == name:
                return True
        return False

    def find_by_id(self, id: int) -> Zone|None:
        for zone in self.zones:
            if zone.id == id:
                return zone
        return None

    def count(self) -> int:
        return len(self.zones)

