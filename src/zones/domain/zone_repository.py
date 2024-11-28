from abc import ABC, abstractmethod
from src.zones.domain.zone import Zone

class ZoneRepository(ABC):
    @abstractmethod
    def save(self, zone: Zone) -> None:
        pass
