from src.zones.domain.zone import Zone

class ZoneCreator:
    def __init__(self, zone_repository) -> None:
        self.zone_repository = zone_repository

    def create(self, id: int, name: str) -> Zone:
        zone = Zone(id=id, name=name)
        self.zone_repository.save(zone)
        return zone
