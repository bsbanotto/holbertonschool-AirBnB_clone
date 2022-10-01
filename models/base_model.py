#!/usr/bin/python3
"""
base_model module for the AirBnB console project
"""
from datetime import datetime, time
import uuid
import models
time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class containing:
    Public id attribute
    Public created_at attribute
    Public updated_at attribute
    __str__ overwrite to print [<class name>] (<self.id>) <self.__dict__>
    Public method save(self)
    Public method to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiate public attributes
        """
        if kwargs:
            for key in kwargs.keys():
                if key == "created_at":
                    setattr(self, key,
                            datetime.strptime(kwargs[key], time_format))
                elif key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(kwargs[key], time_format))
                    continue
                elif key != ('__class__'):
                    setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Override the string to print [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        class_dict = self.__dict__.copy()
        class_dict["__class__"] = self.__class__.__name__
        class_dict["created_at"] = self.created_at.isoformat()
        class_dict["updated_at"] = self.updated_at.isoformat()
        return class_dict
