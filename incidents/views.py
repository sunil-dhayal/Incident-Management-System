from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .create import IncidentCreationForm, IncidentUpdateForm, IncidentSearchForm
from .models import Incident
from django.contrib import messages
from django.views.generic import ListView
from django.utils.decorators import method_decorator

@login_required
def create_incident(request):
    if request.method == 'POST':
        form = IncidentCreationForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reporter = request.user
            incident.save()
            messages.success(request, 'Incident created successfully!')
            return redirect('incidents:incident_list')

        else:
            messages.error(request, 'Error creating incident. Please correct the form below.')
    else:
        form = IncidentCreationForm()
    return render(request, 'incidents/create.html', {'form': form})

class IncidentListView(ListView):
    model = Incident
    template_name = 'incidents/list.html'
    context_object_name = 'incidents'

    @method_decorator(login_required, name='dispatch')
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = Incident.objects.filter(reporter=self.request.user)
        query = self.request.GET.get('search_query')
        if query:
            queryset = queryset.filter(incident_id__icontains=query)
        return queryset.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = IncidentSearchForm(self.request.GET)
        return context

@login_required
def update_incident(request, incident_id):
    incident = get_object_or_404(Incident, incident_id=incident_id, reporter=request.user)

    if incident.status == 'closed':
        messages.error(request, "Closed incidents cannot be edited.")
        return redirect('incidents:incident_list')

    if request.method == 'POST':
        form = IncidentUpdateForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            messages.success(request, 'Incident updated successfully!')
            return redirect('incidents:incident_list')
        else:
            messages.error(request, 'Error updating incident. Please correct the form below.')
    else:
        form = IncidentUpdateForm(instance=incident)
    return render(request, 'incidents/update_incident.html', {'form': form, 'incident': incident})
