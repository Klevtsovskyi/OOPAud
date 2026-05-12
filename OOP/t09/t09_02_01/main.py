from GeneralStaff import GeneralStaff
from MilitaryBase import MilitaryBase
from Saboteur import Saboteur
from SecretAgent import SecretAgent

if __name__ == '__main__':
    general_staff = GeneralStaff("Otkatochna", 4, 12)
    military_base = MilitaryBase("Dacha Vovchika", 12000, 10)
    print(general_staff)
    print(military_base)

    secret_agent = SecretAgent("Shchvechinin")
    saboteur = Saboteur("Bykovska")

    general_staff.accept(secret_agent)
    print(secret_agent)
    military_base.accept(secret_agent)
    print(secret_agent)

    general_staff.accept(saboteur)
    print(saboteur)
    military_base.accept(saboteur)
    print(saboteur)

    print(general_staff)
    print(military_base)

