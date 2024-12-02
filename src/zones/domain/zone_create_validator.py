from src.commons.domain.validation_error import ValidationError
from src.zones.domain.zone_repository import ZoneRepository

class ZoneCreateValidator:
    def __init__(self, zone_repository: ZoneRepository):
        self.zone_repository = zone_repository
        self.errors = {}

    def validate(self, data: dict) -> None:
        self.validate_id(data["id"])
        self.validate_name(data["name"])

        if len(self.errors) > 0:
            raise ValidationError(self.errors)

    def validate_id(self, id: int) -> None:
        if not id is None:
            self.errors["id"] = "Id should be null"

    def validate_name(self, name: str) -> None:
        if name is None or name == "":
            self.errors["name"] = "Name is required"
        elif self.zone_repository.name_already_exists(name) is True:
            self.errors["name"] = "Name already exists"
