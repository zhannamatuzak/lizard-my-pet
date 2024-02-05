from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Lizard, Experience
from .forms import ExperienceForm


from django.contrib.messages.views import SuccessMessageMixin


class LizardList(generic.ListView):
    model = Lizard
    queryset = Lizard.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 6


class LizardDetail(SuccessMessageMixin, View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Lizard.objects.filter(status=1)
        lizard = get_object_or_404(queryset, slug=slug)
        experiences = lizard.experiences.order_by('created_on')
        liked = False
        if lizard.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "blog/lizard_detail.html",
            {
                "lizard": lizard,
                "experiences": experiences,
                "commented": False,
                "liked": liked,
                "experience_form": ExperienceForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Lizard.objects.filter(status=1)
        lizard = get_object_or_404(queryset, slug=slug)
        experiences = lizard.experiences.order_by("-created_on")
        liked = False
        if lizard.likes.filter(id=self.request.user.id).exists():
            liked = True

        experience_form = ExperienceForm(data=request.POST)

        if experience_form.is_valid():
            experience_form.instance.user = request.user
            experience = experience_form.save(commit=False)
            experience.post = lizard
            experience.save()
            messages.success(request, 'Your Experience was Successfully Shared!')
        else:
            experience_form = ExperienceForm()

        return render(
            request,
            "blog/lizard_detail.html",
            {
                "lizard": lizard,
                "experiences": experiences,
                "commented": True,
                "liked": liked,
                "experience_form": ExperienceForm()
            },
        )


class LizardLike(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        lizard = get_object_or_404(Lizard, slug=slug)

        if lizard.likes.filter(id=request.user.id).exists():
            lizard.likes.remove(request.user)
        else:
            lizard.likes.add(request.user)

        return HttpResponseRedirect(reverse('lizard_detail', args=[slug]))


class ExperienceDelete(DeleteView):
    """
    If user is logged in,
    he will be redirected to delete_comment.html template.
    User will be prompted with a message to confirm deletion.
    """
    model = Experience
    template_name = "blog/delete_experience.html"


    def get_success_url(self):
        """Send the user to this url when edit successful"""
        lizard = self.object.post
        lizard_slug = lizard.slug
        messages.success(self.request, "Experience Successfully Deleted")
        return reverse('lizard_detail', kwargs={"slug": lizard_slug})


class ExperienceEdit(UpdateView):
    """
    If user is logged in,
    he will be redirected to update_experience.html template.
    """
    model = Experience
    class_form = ExperienceForm
    template_name = "blog/edit_experience.html"
    fields = ['pet_name', 'size', 'body']

    def test_func(self):
        experience = self.get_object()
        return self.request.user.username == experience.user

    def form_valid(self, form):
        # Call the parent class's form_valid method to perform default actions
        response = super().form_valid(form)

        # Redirect the user to the lizard_detail page with the updated slug
        return HttpResponseRedirect(
            reverse("lizard_detail", kwargs={"slug": self.object.post.slug})
        )

    def get_success_url(self):
        """Send the user to this url when edit successful"""
        lizard = self.object.post
        lizard_slug = lizard.slug
        messages.success(self.request, "Shared experience Successfully Updated")
        return reverse('lizard_detail', kwargs={"slug": lizard_slug})


class Page403(TemplateView):
    template_name = '403.html'


class Page404(TemplateView):
    template_name = '404.html'
