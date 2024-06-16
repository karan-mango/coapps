from django.shortcuts import render, redirect
from .forms import LeadForm
from myapp.decorators import custom_login_required

from django.shortcuts import render, get_object_or_404, redirect
from .models import Lead
from .forms import LeadForm

def edit_lead(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead_list')  # Redirect to the lead list after saving
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads/edit_lead.html', {'form': form, 'lead': lead})


@custom_login_required
def add_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead_list')  # Change 'lead_list' to your desired redirect URL
    else:
        form = LeadForm()
    return render(request, 'leads/lead_form.html', {'form': form})

from .models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})
