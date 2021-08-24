__author__ = "Fuzz"

import pickle
from modules.objectMaker import *
from modules.people import *


def dump_object(object_to_dump):
    if isinstance(object_to_dump, Product):
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

    elif isinstance(object_to_dump, Person):
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


def get_object(object_search, type_search):
    file_db = 'Data/Clients.dat'
    p = open(file_db, 'rb')
    vec = []
    result = None
    condition = True
    while condition:
        try:
            vec.append(pickle.load(p))
        except EOFError:  # End of file error
            condition = False
        finally:
            pass
    if not condition:
        for x in range(0, len(vec)):
            if type_search == "Client":
                if vec[x].doc_type == object_search:
                    result = vec[x]
                else:
                    pass
            elif type_search == "Partner":
                if vec[x].doc_type == object_search:
                    result = vec[x]
                else:
                    pass
            elif type_search == "Product":
                if vec[x].codeProduct == object_search:
                    result = vec[x]
                else:
                    pass
    return result


if __name__ == "__main__":
    print("Object save module")
