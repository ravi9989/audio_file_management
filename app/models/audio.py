from mongoengine import DynamicDocument, IntField, StringField, DateTimeField, DictField, FloatField, BooleanField
from mongoengine.document import Document



class Audio(Document):
    meta = {'allow_inheritance': True}
    Id = IntField(required = True)
    duaration_in_secs = IntField(required = True, min_value = 1)
    uploaded_time = DateTimeField(required = True)
    file_type = StringField(required = True)
    meta = {'abstract': True}



