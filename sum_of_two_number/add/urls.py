from django.urls import path
from add import views

urlpatterns = [
    path('add/', views.operation_add, name="operation_add"),
    path('delete/<int:operation_id>/', views.delete_operstion, name="delete_operstion"),
    path('edit/<int:operation_id>', views.edit_operation, name="edit_operation")
]