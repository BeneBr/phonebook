from pytest import fixture
from Model.user import User
from Model.address import Address

@fixture
def user() -> User:
    address = Address('Barros Cassal','Centro',280,'RS','Alegrete')
    user = User(name='Joao',last_name='Neves',age=50,phone_number=55999897979 ,e_mail='gberned@gmail.com', address=address)

    return user

def testUser(user) -> None:
    assert user != None
    assert user.name == 'Joao' and user.last_name == 'Neves'
    assert user.address.number == 280 and user.address.street == 'Barros Cassal'
    assert user.full_name == 'Joao Neves'
    assert user.e_mail == 'gberned@gmail.com'
    assert not user.contacts == 0

def testUserContacts(user) -> None:
    address = Address('Venancio Aires', 'Centro', 580, 'RS', 'Santa Maria')
    user1 = User(name='Pedro', last_name='Cruzeira', age=75, phone_number=55999897979, e_mail='pedrocru@gmail.com',
                address=address)
    address2 = Address('Bento Manoel', 'Centro', 780, 'RS', 'Porto Alegre')
    user2 = User(name='Ana', last_name='Julia', age=35, phone_number=55999897979, e_mail='anaJulia@gmail.com',
                address=address2)
    user.contacts.append(user1)
    user.contacts.append(user2)

    assert len(user.contacts) == 2