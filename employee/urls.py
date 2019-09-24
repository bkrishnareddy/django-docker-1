
from django.urls import path, include

from rest_framework_mongoengine import routers
from employee.views import EmployeeView

router = routers.DefaultRouter()
router.register(r'employees',EmployeeView)


urlpatterns = []
urlpatterns += router.urls
