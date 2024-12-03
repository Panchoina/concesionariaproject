from django.urls import path
from boleta import views

urlpatterns = [
    path('boleta/<int:folio>/imprimir/', views.ImprimirBoleta, name='imprimir_boleta'),
]