from mongoengine import DynamicDocument, IntField, StringField, DateTimeField, DictField, FloatField, BooleanField
from .audio import Audio 


class Song(Audio):
    title = StringField(required = True, max_length=200)
    meta = {
        "collection": "songs",
        }