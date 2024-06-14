# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('add_account/', views.add_account, name='add_account'),
#     path('add_transaction/<int:account_id>/', views.add_transaction, name='add_transaction'),
#     path('view_transactions/<int:account_id>/', views.view_transactions, name='view_transactions'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_account/', views.add_account, name='add_account'),
    path('add_transaction/<int:account_id>/', views.add_transaction, name='add_transaction'),
    path('view_transactions/<int:account_id>/', views.view_transactions, name='view_transactions'),
    path('delete_account/<int:account_id>/', views.delete_account, name='delete_account'),
]
