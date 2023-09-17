#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
import os
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from sqlalchemy import create_engine


class DBStorage:
    """This class manages storage of hbnb models in mysql db"""
    __engine = None
    __session = None

    def __init__(self) -> None:
        """Instantiate a DBStorage object"""
        self.__engine = create_engine("""mysql+mysqldb://{}:{}@{}/{}"""
                                      .format(
                                          os.getenv('HBNB_MYSQL_USER'),
                                          os.getenv('HBNB_MYSQL_PWD'),
                                          os.getenv('HBNB_MYSQL_HOST'),
                                          os.getenv('HBNB_MYSQL_DB')))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects of a certain class.
        If no class is specified, query all types of objects.
        """
        if not self.__session:
            self.reload()
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
        else:
            classes = [State, City, User, Place, Review]
            objs = []
            for cls in classes:
                objs.extend(self.__session.query(cls).all())
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """
        Add an object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create
        the current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
