from django.db.models.query import Prefetch
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, FormView
from django.db.models import Q
from blog import models
from . import forms


class BlogDetailView(DetailView):
    model = models.Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.object

        older_post = self.model.objects.filter(
            Q(updated_at__lt=post.updated_at)
            | Q(updated_at=post.updated_at, id__lt=post.id)
        ).first()

        newer_post = self.model.objects.filter(
            Q(updated_at__gt=post.updated_at)
            | Q(updated_at=post.updated_at, id__gt=post.id)
        ).last()

        context['older_post'] = older_post
        context['newer_post'] = newer_post

        context['form'] = forms.CommentForm()

        context['comments'] = post.comments.all()

        return context

    def get_queryset(self):
        level_3 = models.Comment.objects.filter(status=True).order_by('created_at')
        level_2 = models.Comment.objects.filter(status=True).order_by('created_at').prefetch_related(
            Prefetch('replies', queryset=level_3)
        )
        level_1 = models.Comment.objects.filter(status=True, parent__isnull=True).order_by(
            '-created_at').prefetch_related(
            Prefetch('replies', queryset=level_2)
        )

        return self.model.objects.prefetch_related(
            Prefetch('comments', queryset=level_1)
        )


class CreateComment(FormView):
    form_class = forms.CommentForm
    template_name = 'blog/blog_detail.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(models.Post, slug=self.kwargs['slug'])

        comment_parent_id = self.request.POST.get('parent')

        if comment_parent_id not in ('', 'None'):
            comment_parent = get_object_or_404(models.Comment, id=comment_parent_id, status=True, post=comment.post)

            depth = 1
            current = comment_parent

            while current.parent_id:
                depth += 1

                current = current.parent

            if depth >= 3:
                form.add_error(None, "امکان پاسخ به این دیدگاه وجود ندارد.")
                return self.form_invalid(form)

            comment.parent = comment_parent

        else:
            comment.parent = None

        comment.save()

        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('blog:blog_detail', kwargs={'slug': self.kwargs['slug']})
