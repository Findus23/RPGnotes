from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.text import slugify
from django.utils.translation import gettext as _

from notes.models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["name", "aliases", "description_md", "parent", "image"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pk = self.instance.pk if self.instance is not None else None
        slug = slugify(name)
        if Note.objects.filter(slug=slug).exclude(pk=pk).exists():
            raise ValidationError(_('A note with this name already exists.'))
        return name
