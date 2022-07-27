from Controller.user_controller import UserController
from Model.address import Address

def testUserController() -> None:
    user_controller = UserController()
    user = user_controller.NewUser('Gustavo', 'Berned', 32, 55991294943)
    assert user.address == None

    user_controller.SetUserAddress(user=user, street='Mariz e Barros', neighborhood='Centro', number=278, state='RS', city='Alegrete')

    assert user.address != None
