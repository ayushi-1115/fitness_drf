from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import WorkoutPlan, Exercise
from django.shortcuts import get_object_or_404

# Helper to restrict to trainers only
def is_trainer(user):
    return getattr(user, 'role', None) == 'trainer'

@method_decorator(login_required, name='dispatch')
class WorkoutPlanListView(ListView):
    model = WorkoutPlan
    template_name = 'workouts/workout_plans.html'
    context_object_name = 'plans'

@method_decorator(login_required, name='dispatch')
class WorkoutPlanDetailView(DetailView):
    model = WorkoutPlan
    template_name = 'workouts/workout_plan_detail.html'
    context_object_name = 'plan'

@method_decorator([login_required, user_passes_test(is_trainer)], name='dispatch')
class WorkoutPlanCreateView(CreateView):
    model = WorkoutPlan
    fields = ['title', 'description', 'level', 'is_public']
    template_name = 'workouts/workout_plan_form.html'
    success_url = reverse_lazy('plan-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Create Workout Plan'
        context['submit_text'] = 'Create'
        return context

@method_decorator([login_required, user_passes_test(is_trainer)], name='dispatch')
class WorkoutPlanUpdateView(UpdateView):
    model = WorkoutPlan
    fields = ['title', 'description', 'level', 'is_public']
    template_name = 'workouts/workout_plan_form.html'
    success_url = reverse_lazy('plan-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Update Workout Plan'
        context['submit_text'] = 'Update'
        return context

@method_decorator([login_required, user_passes_test(is_trainer)], name='dispatch')
class WorkoutPlanDeleteView(DeleteView):
    model = WorkoutPlan
    template_name = 'workouts/workout_plan_confirm_delete.html'
    success_url = reverse_lazy('plan-list')
    context_object_name = 'plan'
