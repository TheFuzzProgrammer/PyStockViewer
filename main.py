from modules.objectMaker import *
from modules.dumper import *
from modules.people import *
import userInterface

liquid = Liquid(7, 2.5, "pepsi", 2, 10)

liquid.set_expiration(True, "12/21")

liquid.is_food(True)

employed = Employed("ThisKey", "5/16", "Carrasco", "Raul", 40245712, "DNI", "3512437173", "raulcarrasco654@gmail.com")

client = Client(178, "alpha", "Villarreal", "Lourdes Aldana", "40963781", "DNI", "3516756480", "luvillarreal@gmail.com")

solid = Solid(17, 3, 90, "Gorra", 500, 10)

dump_object(solid)
dump_object(employed)
dump_object(client)
dump_object(liquid)

userInterface.start()
