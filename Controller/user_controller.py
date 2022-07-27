from Model.user import User
from Model.address import Address

class UserController:

    def NewUser(self,
                name: str,
                last_name: str,
                age:int,
                phone_number:int,
                ) -> User:
        user = User(name=name, last_name=last_name, age=age, phone_number=phone_number)

        return user

    def SetUserAddress(self, user: User,
                        street: str,
                        neighborhood: str,
                        number: int,
                        state: str,
                        city: str) -> None:
        address = Address(street=street, neighborhood=neighborhood, number=number, state=state, city=city)
        user.SetAddress(address=address)