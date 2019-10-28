from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from collegecost_api.models import *
from collegecost_api.views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'colleges', College, 'college')
router.register(r'years', Year, 'year')
router.register(r'products', Cost, 'product')
router.register(r'payments', Payment, 'payment')
router.register(r'users', Users, 'user')
router.register(r'paymenttypes', PaymentType, 'paymenttype')
router.register(r'costtypes', CostType, 'costtype')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register$', register_user),
    url(r'^login$', login_user),
]
