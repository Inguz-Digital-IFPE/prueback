import graphene
from graphene_django import DjangoObjectType
from .models import UserProfile


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile


class Query(graphene.ObjectType):
    list_user = graphene.List(UserProfileType)

    def resolve_list_user(root, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return UserProfile.objects.all()


schema = graphene.Schema(query=Query)
