from django.forms import ModelForm
from . models import User,Post

class Userform(ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        
class Postform(ModelForm):
    class Meta:
        model=Post
        exclude=['host']
        