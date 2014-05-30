# coding=utf-8
# Created 2014 by Janusz Skonieczny

import logging
from google.appengine.ext import ndb
from werkzeug.routing import BaseConverter


class KeyConverter(BaseConverter):

    def __init__(self, map):
        super(KeyConverter, self).__init__(map)
        self.regex = '[a-zA-Z0-9-_]+'

    def to_python(self, value):
        try:
            return ndb.Key(urlsafe=value)
        except Exception as ex:
            logging.warning(ex)
            raise Exception("Could not convert to Key „{}”, type {}".format(value, type(value)))

    def to_url(self, value):
        assert isinstance(value, ndb.Key), "Must be an ndb.Key instance"
        return value.urlsafe()
