__author__ = "Fuzz"

import pickle

from objectMaker import *


def dump_object(object_to_dump):
    if type(object) is Product:
        if object_to_dump.isFood:
            file_db = 'food.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()
        else:
            file_db = 'products.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()
    elif type(object_to_dump) is Person:
        if type(object_to_dump) is Client:
            file_db = 'clients.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()

        elif type(object_to_dump) is Employed:
            file_db = 'partners.dat'
            data = open(file_db, 'ab')
            pickle.dump(object_to_dump, data)
            data.close()
        else:
            pass
    else:
        pass
