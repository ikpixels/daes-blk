from . models import products
from django.contrib.auth.models import User
from django.forms import ModelForm
from PIL import Image
from django import forms
from django.core.files import File

	
class ProductForm(ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = products
        fields = ('category',
                  'item',
                  'price',
                  'new_price',
                  'price_com',
                  'location',
                  'stock',
                  'owner',
                  'specify',
                  'real_name',
                  'phone',
                  'whatsapp',
                  'email',
                  'Dicription',
                  'file',
                  'x',
                  'y',
                  'width',
                  'height')
        labels ={'specify':'If others specify(OPTIONAL)',
                 'price_com':'if price is 12, is it per kg?(OPTIONAL)',
                 'real_name':'Business name/name of farmer',
                 'whatsapp':'If a member need whatsapp  chat with users,put his/her whatsapp number,e.g <strong style="color:rgb(0,0,153);">265993344416</strong> not <s>0993344416</s>(OPTIONAL)',
                }
        widgets = {
            'price_com': forms.TextInput(attrs={'placeholder': 'example:per kg / per g'}),
            'stock':forms.TextInput(attrs={'placeholder': 'example:50kg'}),
        }

    def save(self):
        photo = super(ProductForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo

