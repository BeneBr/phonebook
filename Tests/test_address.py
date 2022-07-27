from Model.address import Address
from pytest import fixture

@fixture
def address() -> Address:
    address = Address('Conde de Porto Alegre','Centro',211,'RS','Alegrete')
    return address

def testAddress(address)-> None:
    assert address != None
    assert address.street == 'Conde de Porto Alegre'
    assert address.neighborhood == 'Centro'
    assert address.number == 211
    assert address.state == 'RS'
    assert address.city == 'Alegrete'

