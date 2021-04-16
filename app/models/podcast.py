from mongoengine import DynamicDocument, IntField, StringField, DateTimeField, DictField, FloatField, BooleanField
from mongoengine.fields import ListField
from .audio import Audio 



class Podcast(Audio):
    title = StringField(required = True, max_length = 200)
    host = StringField(required = True, max_length = 100)
    participents = ListField(field=StringField, max_length=10)
    meta = {
        "collection": "podcasts",
        }





