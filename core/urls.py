from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shows/', login_required(views.ShowListView.as_view()), name='shows'),
    path('show<int:pk>/', login_required(views.ShowDetailView.as_view()), name='detail'),
    path('add-show/', login_required(views.ShowCreateView.as_view()), name='add-show'),
    path('venue/', login_required(views.VenueListView.as_view()), name='venues'),
    path('add-venue/', login_required(views.VenueCreateView.as_view()), name='add-venue'),
    path('artists/', login_required(views.ArtistListView.as_view()), name='artists'),
]
