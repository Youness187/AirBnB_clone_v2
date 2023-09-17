#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
from uuid import uuid4
from datetime import datetime


if getenv("HBNB_TYPE_STORAGE") == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == "created_at" or key == "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == "_sa_instance_state":
                continue
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            dictionary[key] = value
        return dictionary

    def delete(self):
        """
        Delete the current instance from storage
        """
        models.storage.delete(self)
