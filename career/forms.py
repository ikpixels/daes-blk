from . models import job
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm
from PIL import Image
from django import forms
	
class JobForm(ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        body = forms.CharField(widget=CKEditorWidget())
        model = job
        fields = ('category',
                  'title',
                  'orginisaton',
                  'location',
                  'link',
                  'closing_date',
                  'body',
                  'file',
                  'x',
                  'y',
                  'width',
                  'height')
        labels ={'orginisaton':'Orginisaton name',
                  'link':'Web link (OPTIONAL)',
                  'file':'Logo',
                }
        widgets = {
            'closing_date': forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
    
        }

    def save(self):
        photo = super(JobForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo

