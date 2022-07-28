from Model.address import Address
from typing import Optional
from dataclasses import dataclass

@dataclass(init=True)
class User:
    avatar: str
    name: str
    last_name: str
    age: int
    phone_number: int
    address: Optional[Address] = None

    @property
    def full_name(self) -> str:
        return self.name + " " + self.last_name

    def SetAddress(self, address: Address) -> None:
        self.address = Address