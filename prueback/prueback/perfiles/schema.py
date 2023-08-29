import graphene
from graphene_django import DjangoObjectType
from .models import UserProfile
from django.contrib.auth.models import User


class TrueUserType(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ('password',)


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class CreateUser(graphene.Mutation):
    user = graphene.Field(TrueUserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        nombre = graphene.String(required=True)
        apellidos = graphene.String(required=True)
        curp = graphene.String(required=True)
        fecha_nacimiento = graphene.types.datetime.Date(required=True)
        edad = graphene.Int(required=True)

    def mutate(self, info, username, nombre, apellidos, curp,
               fecha_nacimiento, edad, password):

        username = username.strip()
        user = User.objects.create(username=username)
        user.set_password(password)
        perfil = UserProfile.objects.create(user=user)
        perfil.nombre = nombre
        perfil.apellidos = apellidos
        perfil.curp = curp
        perfil.fecha_nacimiento = fecha_nacimiento
        perfil.edad = edad
        user.save()
        perfil.save()

        return CreateUser(user=user)


class DeleteUser(graphene.Mutation):
    confirm = graphene.String()

    class Arguments:
        token = graphene.String(required=True)
        id = graphene.Int(required=True)

    def mutate(self, info, token, id):
        user = info.context.user
        if not user.is_anonymous:
            try:
                User.objects.get(id=id).delete()
                confirm = "User has been successfully deleted"
            except Exception:
                confirm = "User couldn't be deleted"

            return DeleteUser(confirm=confirm)


class EditUser(graphene.Mutation):
    user = graphene.Field(TrueUserType)

    class Arguments:
        token = graphene.String(required=True)
        id = graphene.Int(required=True)
        username = graphene.String()
        password = graphene.String()
        nombre = graphene.String()
        apellidos = graphene.String()
        curp = graphene.String()
        fecha_nacimiento = graphene.types.datetime.Date()
        edad = graphene.Int()

    def mutate(self, info, token, id, username=None, password=None,
               nombre=None, apellidos=None, curp=None,
               fecha_nacimiento=None, edad=None):

        user = info.context.user
        if not user.is_anonymous:
            user = User.objects.get(id=id)

            perfil = UserProfile.objects.get(user=user)
            if username:
                user.username = username
            if password:
                user.password = password
            if nombre:
                perfil.nombre = nombre
            if apellidos:
                perfil.apellidos = apellidos
            if curp:
                perfil.curp = curp
            if fecha_nacimiento:
                perfil.fecha_nacimiento = fecha_nacimiento
            if edad:
                perfil.edad = edad
            user.save()
            perfil.save()

            return EditUser(user=user)


class Query(graphene.ObjectType):
    list_user = graphene.List(TrueUserType,
                              token=graphene.NonNull(graphene.String))

    def resolve_list_user(root, info, token, **kwargs):
        user = info.context.user
        if not user.is_anonymous:
            return User.objects.all()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    edit_user = EditUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
