from django.shortcuts import render
from . models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    success_url = '/smart/notes/'
    form_class = NotesForm
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model = Notes
    success_url = '/smart/notes/'
    template_name = 'notes/notes_confirm_delete.html'
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    

class NotesListView(LoginRequiredMixin ,ListView):
    model = Notes
    template_name = 'notes/list_notes.html'
    context_object_name = 'notes'
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()
    
class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'
    login_url = "/login"
    
    def get_queryset(self):
        return self.request.user.notes.all()
