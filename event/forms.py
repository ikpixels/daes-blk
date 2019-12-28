from . models import events,documents
from django.contrib.auth.models import User
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from PIL import Image
from django import forms

class DocumentForm(ModelForm):
  class Meta:
    model = documents
    fields = ('title', 'docu')
	
class eventForm(ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        body = forms.CharField(widget=CKEditorWidget())
        model = events
        fields = ('title',
                  'Event_date',
                  'asp',
                  'location',
                  'time',
                  'body',
                  'image',
                  'x',
                  'y',
                  'width',
                  'height')
        labels ={'image':'Cover image',
                 'Event_date':'Date of event',
                }
        widgets = {
            'Event_date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'time': forms.TextInput(attrs={'placeholder': 'hr:m:s'}),
        }

    def save(self):
        photo = super(eventForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((1000, 500), Image.ANTIALIAS)
        resized_image.save(photo.image.path)

        return photo

