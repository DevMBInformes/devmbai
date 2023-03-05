#!/bin/python
from .obj_table import obj_sqlite, obj_table
class config_general(obj_table):

    #block of private methods
    def values_default(self)->None: #@abstract
        ''' defines default values the class'''
        self.id = 1
        self.log = 1
        self.lang = "es"
        self.verbose = 0
        self.vvv = 0
        return None
        
    
    def values_table(self)->None: #@abstract
        ''' defines default values the table'''
        self.id = 'ip'
        self.log = 'i'
        self.lang = 't'
        self.verbose = 'i'  
        self.vvv = 'i'
        return None

    #block of properties
    def set_id(self, _id:int)->None:
        ''' set the id''' 
        self.id = _id
        return None
    
    def set_log(self, _log)->None:
        ''' set _log, value 0 or 1 (False or True)'''
        self.log = self.convert_value(_log)
        return None
    
    def set_lang(self, _lang:str)->None:
        ''' defines the languaje'''
        self.lang = _lang[:2]
        return None

    def set_verbose(self, _verbose)->None:
        ''' defines if messages printed on the screen'''
        self.verbose = self.convert_value(_verbose)
        return None
    
    def set_vvv(self, _vvv)->None:
        ''' defines if all message details are printed'''
        self.vvv = self.convert_value(_vvv)
        return None

    def get_values_config(self)->dict:
        ''' get values configs'''
        obj_sql = obj_sqlite(self._data_base)
        result = obj_sql.selectOne(self.get_name(),'id=1')#obtenemos una unica tupla.
        if isinstance(result, dict):
            for key, value in result.items():
                setattr(self, key, value)
        return result

    def record_default_values(self)->bool:
        ''' record default values in the class
            if the exists a field update this field, the number one.
        '''
        self.values_default() # get the default values
        values_default = self.convert_class_to_dict() #convert default values a class
        del values_default['id'] # delete 'id'
        #second part, update or new fields
        obj_sql = obj_sqlite(self._data_base) #create obj.
        count_rows = obj_sql.selectCountRows(self.get_name())
        if count_rows==0:
            result = obj_sql.insert(self.get_name(), values_default)
        else:
            result = obj_sql.update(self.get_name(),values_default, "id=1")
        obj_sql.close()
        return bool(result[0])




