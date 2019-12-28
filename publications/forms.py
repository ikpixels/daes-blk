from . models import videos , cordination
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from PIL import Image
from django import forms
	
class VideoForm(ModelForm):


    class Meta:
        body = forms.CharField(widget=CKEditorWidget())
        model = videos
        fields = (
                  'title',
                  'category',
                  'location',
                  'video',
                 )
        labels ={'video':'youtube video url link',
                 'location':'If event or success stories add its location(OPTIONAL)',
                }
        widgets = {
            'video': forms.TextInput(attrs={'placeholder': 'e.g https://www.youtube.com/watch?v=SVY8I46dkb0'}),
  
        }

class ASPForm(ModelForm):


    class Meta:
        body = forms.CharField(widget=CKEditorWidget())
        model = cordination
        fields = (
                  'asp',
                  'male',
                  'female',
                  'total',
                  'vac_no',
                  'vac_name',
                  'discription'
                 )
        labels ={'asp':'Name of Asp',
                 'male':'Male members',
                 'female':'Female members',
                 'total':'Total membership',
                 'vac_no':'total VACs under this ASP',
                 'vac_name':'Names of VACs(OPTIONAL)'
                }
        widgets = {
            'male': forms.TextInput(attrs={'placeholder': 'total number of male'}),
            'female': forms.TextInput(attrs={'placeholder': 'total number of female'}),
            'vac_name': forms.TextInput(attrs={'placeholder': 'e.g Kapalamula,Amidu'}),
  
        }

