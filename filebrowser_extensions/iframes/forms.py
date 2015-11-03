from django import forms
from .models import IFrame


class IFrameAdminForm(forms.ModelForm):
    """
    IFrame form used to modify widget of `code` field
    """

    class Meta:
        model = IFrame
        fields = ('name', 'code', 'thumbnail')
        widgets = {
            'code': forms.Textarea
        }
