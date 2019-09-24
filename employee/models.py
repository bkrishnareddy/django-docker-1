
from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


class Projects(EmbeddedDocument):
    projectId = fields.StringField(max_length = 10, required=True, null= False)
    name = fields.StringField(max_length = 20, required=True, null=False)

class Skills(EmbeddedDocument):
    tech = fields.StringField(max_length = 10, required=True, null= False)
    experience = fields.StringField(max_length = 20, required=True, null=False)
    level = fields.IntField()

class Employee(Document):
    empId = fields.StringField(max_length = 10, required=True, null= False)
    name = fields.StringField(max_length = 20, required=True, null=False)
    workLocation = fields.StringField(max_length = 10, required=True, null= False)
    projects = fields.EmbeddedDocumentListField(Projects)
    skills = fields.EmbeddedDocumentListField(Skills)
