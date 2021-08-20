
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='APIV1')

app_name = "apiv1"

urlpatterns = [

    path('doc/', schema_view)
]
