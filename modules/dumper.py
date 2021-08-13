__author__ = "Fuzz"

import pickle
from modules.objectMaker import *
from modules.people import *


def dump_object(object_to_dump):
    if (type(object_to_dump) is Liquid) or (type(object_to_dump) is Solid):
        if object_to_dump.isFood:
            file_db = 'Data/Food.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()
        else:
            file_db = 'Data/Products.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()

    elif type(object_to_dump) is Person:
        if type(object_to_dump) is Client:
            file_db = 'Data/Clients.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()

        elif type(object_to_dump) is Employed:
            file_db = 'Data/Partners.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()
        else:
            pass
    else:
        pass


if __name__ == "__main__":
    print("Object save module")
