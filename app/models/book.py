from mongoengine import DynamicDocument, IntField, StringField, DateTimeField, DictField, FloatField, BooleanField
from .audio import Audio 


class Book(Audio):
    title = StringField(required = True, max_length=200)
    narrator = StringField(required = True, max_length=100)
    author = StringField(required = True, max_length=100)
    meta = {
        "collection": "audio_books",
        }



