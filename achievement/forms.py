from . models import achievement
from django.contrib.auth.models import User
from django.forms import ModelForm
from PIL import Image
from django import forms
from ckeditor.widgets import CKEditorWidget
	
class achievementForm(ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        body = forms.CharField(widget=CKEditorWidget())
        model = achievement
        fields = ('title',
                  'body',
                  'image',
                  'x',
                  'y',
                  'width',
                  'height')
        """labels ={'madeIN':'Is this item made in Malawi?',
                  'color':'Available colors (OPTIONAL)',
                  'sizes':'Available size (OPTIONAL)',
                  'Dicription':'Discription (OPTIONAL)',
                }
        widgets = {
            'color': forms.TextInput(attrs={'placeholder': 'Separate item colors with comma e.g red,black,green'}),
            'sizes': forms.TextInput(attrs={'placeholder': 'Separate item size with comma e.g 2,5 or X,ML,M'}),
            'stock': forms.TextInput(attrs={'placeholder': 'Put zero if you dont want your customer to add this item to buskcate'}),
        }"""

    def save(self):
        photo = super(achievementForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((1000, 500), Image.ANTIALIAS)
        resized_image.save(photo.image.path)

        return photo

