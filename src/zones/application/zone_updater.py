from src.zones.domain.zone import Zone

class ZoneUpdater:
    def __init__(self, zone_repository):
        self.zone_repository = zone_repository

    def update(self, zone: Zone, data: dict) -> Zone:
        return zone
