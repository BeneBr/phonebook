from Model.address import Address
from typing import Optional, List
from dataclasses import dataclass


class UserContacts:
    pass


@dataclass(init=True)
class User:
    name: str
    last_name: str
    age: int
    phone_number: int
    e_mail: str
    address: Optional[Address] = None
    contacts = []

    @property
    def full_name(self) -> str:
        return self.name + " " + self.last_name

    def SetAddress(self, address: Address) -> None:
        self.address = address

@dataclass
class UserContacts:
    user_contacts: Optional[List[User]] = None
    
    def GetUserContacts(self) -> List[User]:
        return self.user_contacts