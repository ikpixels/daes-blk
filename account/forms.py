from . models import partners,TeamMember
from django.contrib.auth.models import User
from django.forms import ModelForm
from PIL import Image
from django import forms
from django.core.files import File

	
class PartinersForm(ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = partners
        fields = (
                  'name',
                  'link',
                  'file',
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
        photo = super(PartinersForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo

class TeamForm(ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = TeamMember
        fields = (
                  'name',
                  'cordination',
                  'specify',
                  'position',
                  'Orgnisation',
                  'desination',
                  'phone',
                  'whatsapp',
                  'email',
                  'facebook',
                  'linkedin',
                  'description',
                  'file',
                  'x',
                  'y',
                  'width',
                  'height')
        labels ={'specify ':'Other cordination(OPTIONAL)',
                 'facebook':'facebook link(OPTIONAL)',
                 'linkedin':'linkedin link(OPTIONAL)',
                 'whatsapp':'If a member need whatsapp  chat with users,put his/her whatsapp number,e.g <strong style="color:rgb(0,0,153);">265993344416</strong> not <s>0993344416</s>(OPTIONAL)',
                  
                }
        widgets = {
            'specify': forms.TextInput(attrs={'placeholder': 'e.g name of vac'}),
            'facebook': forms.TextInput(attrs={'placeholder':'https://your fb link.com/?_rdc=1&_rdr'}),
            'linkedin': forms.TextInput(attrs={'placeholder': 'https://your linkin link.com/?_rdc=1&_rdr'}),
            'linkedin': forms.TextInput(attrs={'placeholder': 'e.g 265993344416 not 0993344416'}),
            
        }

    def save(self):
        photo = super(TeamForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo

