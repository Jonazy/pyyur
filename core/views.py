from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Venue, Show
from django.views import generic
from django.shortcuts import get_object_or_404
from .forms import VenueForm, ShowForm


# Create your views here.

# Landing page function
def home(request):
    template_name = 'index.html'
    if request.method == 'GET':
        context = {

        }
        return render(request, template_name, context)


class ShowListView(generic.ListView):
    model = Show
    queryset = Show.objects.all()
    context_object_name = 'show_listings'
    template_name = 'show/show_list.html'


class ShowCreateView(generic.CreateView):
    model = Show
    fields = '__all__'
    context_object_name = 'add_show'
    template_name = 'show/add_show.html'
    success_url = '/show'


class ShowDetailView(generic.DetailView):
    # queryset = get_object_or_404(Show, id=id)
    queryset = Show.objects.all()
    context_object_name = 'show_detail'
    template_name = 'show/show_detail.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['past_show'] = "past_show"
    #     return context


class VenueListView(generic.ListView):
    model = Venue
    context_object_name = 'venue_listings'
    template_name = 'venue/venue_list.html'


class VenueCreateView(generic.CreateView):
    model = Venue
    form_class = VenueForm
    context_object_name = 'add_venue'
    template_name = 'venue/add_venue.html'
    success_url = '/venue'


class VenueDetailView(generic.DetailView):
    # queryset = get_object_or_404(Venue, id=id)
    queryset = Venue.objects.all()
    context_object_name = 'venue_detail'
    template_name = 'venue/venue_detail.html'
