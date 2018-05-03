from django.conf.urls import url
from .views import order_list

urlpatterns =[
    url(r'order-list' , order_list ),
]
