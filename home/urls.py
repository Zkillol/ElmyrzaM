from django.urls import path
from .views import couuntry_list_view, country_list_detail_view , country_detail_view

urlpatterns = [
    path('country_list/', couuntry_list_view),
    path('country_list/<int:id>/', country_list_detail_view),
    path('detail/',country_detail_view , name = 'detail' )
]
