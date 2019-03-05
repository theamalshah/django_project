from django.forms import ModelForm
from .models import user

class adduser(ModelForm):
	class Meta:
		model=user
		fields=['name','password']
		