#!/usr/bin/env python3

import os
import json
import cgutils
from dbobject_ifc import DBObjectInterface


# Access DB Object with cash
class JsonDBObject(DBObjectInterface):
    def __init__(self, name, filepath) -> None:
        super.__init__(self)
        self.name = name
        self.filepath = filepath
        
    
    def __read_json(self):
        data = dict()
        if (self.filepath):
            try:
                with open(self.filepath, 'r') as file:
                    data = json.load(file)
                    return data
            except Exception:
                self.logger.error(f'Failed to load {self.name} from {self.filepath}', exc_info = True)
        else:
            self.logger.error(f'Failed to load {self.name} from {self.filepath}')
        return None
        
    # Read from Json file and find object by Id
    def __get_db(self, id: int): 
        data = self.__read_json()
        if data and id in data:
            return self.data[id]
        else:
            self.logger.error(f'Object {self.name} id {id} not found')
            return None

    # Write to Json data and file
    def __set_db(self, id: int, db_obj) -> bool:
        try:
            with open(self.env_file, 'w') as file:
                data = json.load(file)
                data[id] = db_obj
                json.dump(self.data, file, indent = 4)
                return True
        except Exception:
            self.logger.error(f'Failed to load {self.name} from {self.filepath}', exc_info = True)
        
        return False
