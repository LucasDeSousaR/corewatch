from mongoengine import *

connect(db='corewatch_db', host='localhost', port=27017)

class User(Document):
    idUser = IntField(primary_key=True)
    userName = StringField(max_length=100, required=True)
    userEmail = StringField(max_length=100, required=True)
    userPwd = StringField(max_length=16, required=True)

class Admin(Document):
    idAdmin = IntField(primary_key=True)
    idUser = ReferenceField(User, required=True)

class GroupsTeams(Document):
    idGroup = IntField(primary_key=True)
    description = StringField(max_length=100)

class UserInGroup(Document):
    idGroup = ReferenceField(GroupsTeams, required=True)
    idUser = ReferenceField(User, required=True)

class Lpar(Document):
    idLpar = IntField(primary_key=True)
    nameLpar = StringField(max_length=10, required=True)
    account = StringField(max_length=50)
    ip = StringField(max_length=16)
    luname = StringField(max_length=20)
    lparEnv = StringField(max_length=20)

class Resource(Document):
    idResource = IntField(primary_key=True)
    idLpar = ReferenceField(Lpar, required=True)
    nameResource = StringField(max_length=20)
    value = FloatField()
    resourceDescription = StringField(max_length=100)

class History(Document):
    idHistory = IntField(required=True, unique=True)
    idLpar = ReferenceField(Lpar, required=True)
    uso_cpu = FloatField(required=True)
    uso_msu = FloatField(required=True)
    valor_smf = FloatField(required=True)
    timestamp = DateTimeField(required=True)

class Alert(Document):
    idAlert = IntField(required=True, unique=True)
    idLpar = ReferenceField(Lpar, required=True)
    type = StringField(required=True)
    message = StringField(required=True)
    level = StringField(required=True)
    timestamp = DateTimeField(required=True)

class Dashboard(Document):
    idDashboard = IntField(required=True, unique=True)
    idLpar = ReferenceField(Lpar, required=True)
    resumo = StringField()
    status = StringField()
