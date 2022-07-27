from pytest import fixture
from Model.user import User
from Model.address import Address

@fixture
def user() -> User:
    address = Address('Barros Cassal','Centro',280,'RS','Alegrete')
    user = User('Joao','Neves',50,55999897979,address=address)

    return user

def testUser(user) -> None:
    assert user != None
    assert user.name == 'Joao' and user.last_name == 'Neves'
    assert user.address.number == 280 and user.address.street == 'Barros Cassal'
    assert user.full_name == 'Joao Neves'
