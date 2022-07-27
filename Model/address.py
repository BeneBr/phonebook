from dataclasses import dataclass


@dataclass(init=True, repr=True)
class Address:
    street: str
    neighborhood: str
    number: int
    state: str
    city: str