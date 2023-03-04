#!/bin/python
from .obj_sqlite import obj_sqlite

class obj_table:

    def __init__(self, data_base):
        self._data_base = data_base


    #overridden methods

    def values_default(self)->None:
        ''' instance of default's values '''
        ''' this method should be overridden'''
        return None

    def values_table(self)->None:
        ''' instance of defaul's values of table '''
        ''' this method should be overridden'''
        return None

   #block of private methods
    def default_values(self)->None: #@abstract
        ''' defines default values the class'''
        ''' this method should be overridden'''
        return None
        
    
    def default_values_table(self)->None: #@abstract
        ''' defines default values the table'''
        ''' this method should be overridden'''
        return None


    def convert_class_to_dict(self)->dict:
        ''' convert the class in dict '''
        dict_class = self.__dict__.copy()
        del dict_class['_data_base']
        return dict_class


    def convert_value(self, value)->int:
        ''' set the values to 1 or 0, so that no errors are generated'''
        if isinstance(value, bool):
            value = int(value)
        if isinstance(value, int):
            value = 1 if value >= 1 else 0
        return value

    def get_name(self)->str:
        ''' return name class'''
        return self.__class__.__name__

    def create_table(self)->bool:
        ''' create the table '''
        obj_sql = obj_sqlite(self._data_base) #create object obj_sqlite
        self.values_table() # get default values in the class
        print(self.convert_class_to_dict())
        print(self.get_name())
        result = obj_sql.create_table(self.get_name(), self.convert_class_to_dict()) # create table
        obj_sql.close() # close object sqlite
        return result # return boolean

    def record_default_values(self):
        ''' record default values in the class '''
        self.values_default()
        values_default = self.convert_class_to_dict()
        print(values_default)
        del values_default['id']
        print(self._data_base)
        obj_sql = obj_sqlite(self._data_base)
        print(self.get_name)
        obj_sql.insert(self.get_name(), values_default)

        

    def set_default_values(self):
        pass
        

