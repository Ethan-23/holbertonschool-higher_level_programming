#!/usr/bin/python3
"""
This is the Base Class for the rectangle and the square class
This has all the base functions for other classes
"""
import json


class Base:
    """This is the Base class that will be built off of by other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''json'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save'''
        new_dict = []
        if list_objs is None:
            with open('{}.json'.format(cls.__name__), 'w') as file:
                string = cls.to_json_string(new_dict)
                file.write(new_dict)
        else:
            for i in list_objs:
                new_dict.append(cls.to_dictionary(i))
            with open('{}.json'.format(cls.__name__), 'w') as file:
                file.write(cls.to_json_string(new_dict))

    @staticmethod
    def from_json_string(json_string):
        '''json string'''
        new_list = []
        if json_string is None:
            return new_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create'''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''load'''
        new_list = []
        try:
            with open('{}.json'.format(cls.__name__), 'r') as file:
                thing = from_json_string(read(file))
            for i in thing:
                new_list.append(cls.create(**i))
        except:
            pass
        return new_list
