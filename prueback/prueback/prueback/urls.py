from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    # This URL will provide a user interface that is used to query the database
    # and interact with the GraphQL API.
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
