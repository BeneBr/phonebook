from dataclasses import dataclass
from Model.address import Address


@dataclass(init=True,repr=True, frozen=True)
class User:
    name: str
    last_name: str
    age: int
    phone_number: int
    address: Address

    @property
    def full_name(self) -> str:
        return self.name + " " + self.last_name