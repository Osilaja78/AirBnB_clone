#!/usr/bin/python3
"""
A class BaseModel for other models
to inherit from.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """A new base class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new model"""

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(
                                v, '%Y-%m-%dT%H:%M:%S.%f'
                            ))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the model"""

        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__
            )

    def save(self):
        """
        Updates the public instance attribute
        "updated_at" with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returnd a dictionary representation
        of the instance.
        """

        copy = self.__dict__.copy()
        copy['__class__'] = type(self).__name__

        if 'created_at' in copy and isinstance(copy['created_at'], datetime):
            copy['created_at'] = copy['created_at'].isoformat()

        if 'updated_at' in copy and isinstance(copy['updated_at'], datetime):
            copy['updated_at'] = copy['updated_at'].isoformat()

        return copy
