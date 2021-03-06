"""Imports."""
from django.forms import ModelForm

from .models import Album, Photo


class AlbumForm(ModelForm):
    """Class for Album form."""

    class Meta:
        """
        Form meta class.
        """

        model = Album
        fields = ['cover', 'photos', 'title', 'description', 'published']

    def __init__(self, *args, username=None, **kwargs):
        """Self init."""
        super().__init__(*args, **kwargs)
        self.fields['cover'].queryset = Photo.objects.filter(
            album__user__username=username)
        self.fields['photos'].queryset = Photo.objects.filter(
            album__user__username=username)


class PhotoForm(ModelForm):
    """Class for Photo form."""

    class Meta:
        """
        Form meta class.
        """

        model = Photo
        fields = ['title', 'description', 'image', 'published']

    def __init__(self, *args, username=None, **kwargs):
        """Self init."""
        super().__init__(*args, **kwargs)


class EditPhotoForm(ModelForm):
    """Class for Photo form."""

    class Meta:
        """
        Form meta class.
        """

        model = Photo
        fields = ['title', 'description', 'published']

    def __init__(self, *args, username=None, **kwargs):
        """Self init."""
        super().__init__(*args, **kwargs)


class EditAlbumForm(ModelForm):
    """Class for Photo form."""

    class Meta:
        """
        Form meta class.
        """

        model = Album
        fields = ['cover', 'photos', 'title', 'description', 'published']

    def __init__(self, *args, username=None, **kwargs):
        """Self init."""
        super().__init__(*args, **kwargs)
