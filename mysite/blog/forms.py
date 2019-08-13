from django import forms
from .models import Post

#nombre del formulario y es un ModelForm
class PostForm(forms.ModelForm):
#que modelo debe ser utilizado para crear este formulario model=Post
    class Meta:
        model = Post
        fields = ('title', 'text',) #campos del formulario
        
