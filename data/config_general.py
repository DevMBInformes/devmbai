#!/bin/python
from .obj_table import obj_table
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
        self._lang = _lang[:2]
        return None

    def set_verbose(self, _verbose)->None:
        ''' defines if messages printed on the screen'''
        self.verbose = self.convert_value(_verbose)
        return None
    
    def set_vvv(self, _vvv)->None:
        ''' defines if all message details are printed'''
        self.vvv = self.convert_value(_vvv)
        return None

    
