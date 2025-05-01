from abc import ABC, abstractmethod
from src.zones.domain.zone import Zone

class ZoneRepository(ABC):
    @abstractmethod
    def save(self, zone: Zone) -> None: ...

    @abstractmethod
    def update(self, zone: Zone) -> None: ...

    @abstractmethod
    def name_already_exists(self, name: str) -> bool: ...

    @abstractmethod
    def find_by_id(self, id: int) -> Zone|None: ...

    @abstractmethod
    def count(self) -> int: ...
