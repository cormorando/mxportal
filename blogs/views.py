from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from blogs.models import Entry
from comments.forms import CommentForm


class EntryListView(LoginRequiredMixin, ListView):

    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class EntryDetailView(LoginRequiredMixin, FormMixin, DetailView):

    model = Entry
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_success_url(self):
        return reverse('entry-detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.content_object = self.object
        comment.body = form.cleaned_data['body']
        comment.save()

        return super().form_valid(form)
