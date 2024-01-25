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
from .forms import ExperienceForm, EditForm

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
        experiences = lizard.experiences.filter(approved=True).order_by('created_on')
        liked = False
        if lizard.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "lizard_detail.html",
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
        experiences = lizard.experiences.filter(approved=True).order_by("-created_on")
        liked = False
        if plant.likes.filter(id=self.request.user.id).exists():
            liked = True

        experience_form = ExperienceForm(data=request.POST)

        if experience_form.is_valid():
            experience_form.instance.pet_name = request.user.pet_name
            experience_form.instance.size = request.user.size
            experience = experience_form.save(commit=False)
            experience.post = lizard
            experience.save()
            messages.success(request, 'Your Experience was Successfully Shared!')
        else:
            experience_form = ExperienceForm()

        return render(
            request,
            "lizard_detail.html",
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


class ExperienceDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    If user is logged in,
    he will be redirected to delete_comment.html template.
    User will be prompted with a message to confirm deletion.
    """
    model = Experience
    template_name = "delete_experience.html"

    def test_func(self):
        experience = self.get_object()
        return self.request.user.username == experience.name

    def delete(self, request, *args, **kwargs):
        return super(ExperienceDelete, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        LizardDetail.experience_deleted = True
        messages.success(self.request, 'Your experience has been deleted.')
        return reverse("lizard_detail", kwargs={"slug": self.object.post.slug})


class ExperienceEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    If user is logged in,
    he will be redirected to update_experience.html template.
    """
    model = Experience
    form_class = EditForm
    template_name = "edit_experience.html"

    def test_func(self):
        experience = self.get_object()
        return self.request.user.username == experience.name

    def form_valid(self, form):
        """
        After successful completion, display a success message to the user
        """
        super().form_valid(form)
        messages.success(self.request, 'Your shared experience has been edited.')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        """
        After success, the user will be returned to the post/lizard detail page.
        """
        PlantDetail.comment_edited = True
        return reverse("lizard_detail", kwargs={"slug": self.object.post.slug})


class Page403(TemplateView):
    template_name = '403.html'


class Page404(TemplateView):
    template_name = '404.html'


class Page500(TemplateView):
    template_name = '500.html'