from . models import Projects
from django.contrib.auth.models import User
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from PIL import Image
from django import forms
	
class PJForm(ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        body = forms.CharField(widget=CKEditorWidget())
        model = Projects
        fields = ('name',
                  'NGO',
                  'area',
                  'areas',
                  'PJ_link',
                  'body',
                  'docu',
                  'image',
                  'x',
                  'y',
                  'width',
                  'height')
        labels ={'area':'Target area',
                  'areas':'If more than one target area (OPTIONAL)',
                  'pdf':'Progress report (OPTIONAL)',
                  'PJ_link':'Projects page link (OPTIONAL)',
                }
        widgets = {
            'areas': forms.TextInput(attrs={'placeholder': 'Separate area with comma e.g Amidu,Toleza,Sawali'}),
        }

    def save(self):
        photo = super(PJForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((1000, 500), Image.ANTIALIAS)
        resized_image.save(photo.image.path)

        return photo

