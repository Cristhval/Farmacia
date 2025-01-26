from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class RegistroUsuarioForm(UserCreationForm):
    """
    Formulario personalizado para registrar nuevos usuarios basado en el modelo Usuario.
    """

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'rol']  # Agrega los campos necesarios

    def __init__(self, *args, **kwargs):
        """
        Personalización del formulario, como agregar placeholders o clases CSS.
        """
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nombre de usuario'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Correo electrónico'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirmar contraseña'})
