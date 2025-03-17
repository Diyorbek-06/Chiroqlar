from django.urls import path
from .views import  ChiroqList, ChiroqDetail, ChiroqCreate, ChiroqUpdate, ChiroqDelete, home_page
urlpatterns = [
    path('', home_page, name='home'),
    path('list/', ChiroqList.as_view(), name='chiroq-list'),
    path('chiroq/<int:pk>', ChiroqDetail.as_view(), name='chiroq-detail'),
    path('chiroq-create', ChiroqCreate.as_view(), name='chiroq-create'),
    path('chiroq-update/<int:pk>/', ChiroqUpdate.as_view(), name='chiroq-update'),
    path('chiroq-delete/<int:pk>/', ChiroqDelete.as_view(), name='chiroq-delete'),
    ]