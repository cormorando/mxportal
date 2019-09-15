from django.shortcuts import render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from articles.models import Article
from comments.forms import CommentForm

from articles.tasks import increment_comments


class ArticleListView(LoginRequiredMixin, ListView):

    model = Article

    def get_queryset(self):
        queryset = Article.published.all()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ArticleDetailView(LoginRequiredMixin, FormMixin, DetailView):

    model = Article
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)

        return context

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.pk})

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

        increment_comments.delay(self.object.pk)

        return super().form_valid(form)
