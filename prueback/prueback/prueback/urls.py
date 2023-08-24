from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from perfiles.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    # This URL will provide a user interface that is used to query the database
    # and interact with the GraphQL API.
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]
