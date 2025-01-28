from django import forms
from .models import Pedido
from usuarios.models import Cliente
from inventario.models import Sucursal


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'sucursal_origen', 'sucursal_destino', 'opcion_entrega']
        widgets = {
            'opcion_entrega': forms.RadioSelect(choices=Pedido.OPCIONES_ENTREGA)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['cliente'].queryset = Cliente.objects.all()


        self.fields['sucursal_origen'].queryset = Sucursal.objects.all()
        self.fields['sucursal_destino'].queryset = Sucursal.objects.all()


        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        sucursal_origen = cleaned_data.get('sucursal_origen')
        sucursal_destino = cleaned_data.get('sucursal_destino')

        if sucursal_origen and sucursal_destino and sucursal_origen == sucursal_destino:
            raise forms.ValidationError("La sucursal de origen y destino no pueden ser la misma.")

        return cleaned_data
