# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from notes.forms import NoteForm
from notes.models import Note


def list_note_redirect(request, *args, **kwargs):
    first_note: Note = Note.objects.first()
    if not first_note:
        return redirect("noteadd")
    return redirect(first_note)


class NoteDetailView(generic.DetailView):
    template_name = "notes/detail.html"
    model = Note
    context_object_name = "note"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["roots"] = Note.objects.with_tree_fields()
        return data


class NoteCreateView(generic.CreateView):
    template_name = "loot/edit.html"
    model = Note
    form_class = NoteForm
    context_object_name = "object"


class NoteEditView(generic.UpdateView):
    template_name = "loot/edit.html"
    model = Note
    form_class = NoteForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class NoteDeleteView(generic.DeleteView):
    template_name = "common/confirm_delete.html"
    model = Note
    success_url = reverse_lazy('notelist')
