from modules.objectMaker import *
from modules.dumper import *
from modules.people import *

liquid = Liquid(7, 2.5, "pepsi", 2, 10)

liquid.set_expiration(True, "12/21")

liquid.is_food(True)

dump_object(liquid)

