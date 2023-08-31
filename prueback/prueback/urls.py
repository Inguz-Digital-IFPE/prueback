from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
