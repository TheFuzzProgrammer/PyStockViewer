__author__ = "Fuzz"

import pickle

import objectMaker

def dump_object(object):
    if type(object) is Product:
        if object.isFood:
            file_db = 'food.dat'
            data = open(file_db, 'ab')
            pickle.dump(object, data)
            data.close()
        else:
            file_db = 'products.dat'
            data = open(file_db, 'ab')
            pickle.dump(object, data)
            data.close()
    elif type(object) is Person:
        if type(object) is Client:
            file_db = 'clients.dat'
            data = open(file_db, 'ab')
            pickle.dump(object, data)
            data.close()

        elif type(object) is Employed:
            file_db = 'partners.dat'
            data = open(file_db, 'ab')
            pickle.dump(object, data)
            data.close()
        else:
            pass
    else:
        pass
