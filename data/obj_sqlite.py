#!/bin/python
import sqlite3
from sqlite3 import Error


class obj_sqlite:

    __database = '' # Nombre de base de datos

    #__con = None       # conector
    #__types soportados principalmente por Sqlite3
    __types ={  'I' : 'INTEGER',
                'R' : 'REAL',
                'T' : 'TEXT',
                'B' : 'BLOB',
                'P' : 'PRIMARY KEY',
                'U' : 'UNIQUE'
             }

    def __init__(self, database, con=True):
        ''' initialize the class with the name of the database as a parameter '''
        self.__database = database
        if con == True:
            self.sql_connection()


    def sql_connection(self):
        ''' connect white database'''
        try:
            self.__con = sqlite3.connect(self.__database)
        except Error:
            print(Error)

    
    def sql_execute(self, sql:str, lastrow='0')->list:
        ''' sql execute'''
        _cursorObj = self.__con.cursor()
        try:
            _cursorObj.execute(sql)
            self.__con.commit()
            if lastrow=='0':
                return [True, _cursorObj.lastrowid]
            else:
                return [True, True]
        except Error as err:
            return [False, err]

    
    def sql_query(self, sql:str)->list:
        _cursorObj = self.__con.cursor()
        try:
            _cursorObj.execute(sql)
            rows = _cursorObj.fetchall()
            return rows
        except Error as err:
            return [err]

    def sql_query_with_names(self, sql, many=True)->dict:
        _cursorObj = self.__con.cursor()
        try:
            _cursorObj.execute(sql)
            name_fields = [descripcion[0] for descripcion in _cursorObj.description]
            rows = _cursorObj.fetchall() if many else _cursorObj.fetchone()
            _todict = {name_fields[i]: rows[i] for i in range(len(name_fields))}
            return _todict
        except Error as err:
            error_dict = {}
            error_dict['error'] = err
            return error_dict
            
     

    def delete(self, table, _value, column='id'):
        _sql = "DELETE FROM {} WHERE {} = ".format(table, column)
        if isinstance(_value, int):
            _sql += str(_value)
        else:
            _sql += '\"{}\"'.format(_value)
        return self.sql_execute(_sql)

    def insert(self, table:str, values:dict)->list:
        _sql = "INSERT INTO {} ".format(table)
        _fields = ''
        _values = ''
        _SEP = ', '
        for k, v in values.items():
            _fields += k + _SEP
            if isinstance(v, str):
                _values += '\"' + v + '\"' + _SEP
            else:
                _values += str(v) + _SEP
        _fields = _fields[:-len(_SEP)]
        _values = _values[:-len(_SEP)]
        _sql += "({}) values ({})".format(_fields, _values)
        return self.sql_execute(_sql)


    def selectAll(self, table, columns='*'):
        _sql = "SELECT {} from {}".format(columns, table)
        result = self.sql_query(_sql)
        return result


    def selectCountRows(self, table:str)->int:
        _sql = "SELECT * FROM {};".format(table)
        result = len(self.sql_query(_sql))
        return result


    def selectWhere(self, table:str, cond:str, columns='*'):
        ''' make a sql query select {column='*'} from {table} where {cond}'''
        _sql = "SELECT {} from {} WHERE {}".format(columns, table, cond)
        result = self.sql_query(_sql)
        return result

    def selectOne(self, table, cond):
        _sql = "SELECT * from {} WHERE {}".format(table, cond)
        result = self.sql_query_with_names(_sql, many=False)
        return result


    def update(self, table:str, values:dict, cond:str):
        '''
            table: str, name of table
            values : dict with values
            cond: conditions for update de row
        '''
        _sql = "UPDATE {} \nSET\n".format(table)
        _v_int = ''
        for k, v in values.items():
            if isinstance(v, int):
                _v_int += '\t{} = {},\n'.format(k, str(v))
            else:
                _v_int += '\t{} = \"{}\",\n'.format(k, str(v))
        _sql += _v_int[:-2]
        _sql += "\nWHERE {}".format(cond)
        return self.sql_execute(_sql, lastrow="1")
        



    def create_table(self, table:str, fields:dict)->bool:
        ''' Function for make the tables on database'''
        tmpCad = ''
        for k, v in fields.items():
            tmpCad += k + ' ' + v + ','
        dict_table = {table : tmpCad[:-1]}
        return bool(self.create_tables(dict_table))


    def create_tables(self, dict_tables):
        ''' create a group of table with a dictonary '''
        _fullSql = []
        for k, value in dict_tables.items():
            _sql = 'CREATE TABLE IF NOT EXISTS {} '.format(k)
            fields = value.split(",")
            code_int = ''
            for field in fields:
                field = field.strip(' ')
                detail = field.split(" ")
                code_int += detail[0]
                for nKey in str(detail[1]).upper():
                    code_int += ' ' + self.__types[nKey]
                code_int += ','
            code_int = code_int[:-1]
            _sql += '(' + code_int + ')'
            _fullSql.append(_sql)
        for table in _fullSql:
            self.sql_execute(table)
        return True
    



    def close(self):
        self.__con.close()

