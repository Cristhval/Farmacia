from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'sucursal_origen', 'sucursal_destino', 'opcion_entrega']
        widgets = {
            'opcion_entrega': forms.RadioSelect(choices=Pedido.OPCIONES_ENTREGA)
        }
