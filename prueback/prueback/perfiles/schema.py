import graphene
from graphene_django import DjangoObjectType
from .models import UserProfile
from django.contrib.auth.models import User


class TrueUserType(DjangoObjectType):
    class Meta:
        model = User


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

    def mutate(info, self, username, nombre, apellidos, curp,
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
        username = graphene.String(required=True)

    def mutate(self, info, username):
        try:
            User.objects.get(username=username).delete()
            confirm = "User has been successfully deleted"
        except Exception:
            confirm = "User couldn't be deleted"

        return DeleteUser(confirm=confirm)


class Query(graphene.ObjectType):
    list_user = graphene.List(UserProfileType)

    def resolve_list_user(root, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return UserProfile.objects.all()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
