from rest_framework import routers
from django.urls import path, include
from . import views
from .admin import admin_site

# schema_view = get_schema_view(
#     openapi.Info(
#         title="ChatChit API",
#         default_version='v1',
#         description="APIs for ChatChitApp",
#         contact=openapi.Contact(email="hau.nt@ou.edu.vn"),
#         license=openapi.License(name="Dương Hữu Thành@2021"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

router = routers.DefaultRouter()
router.register('messages', views.MessageViewSet, basename="messages")

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name='index'),
    path('admin/', admin_site.urls)
]