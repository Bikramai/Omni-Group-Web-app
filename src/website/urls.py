from django.urls import path
# from .views import set_language
from .views import (
    ProjectDetailView, ProjectListView, TeamView, AboutUsView, ContactUsView, HomeView,
    ServicesImportsView, ServicesTradersView, ServicesEnterprisesView, ServicesLogisticsView,
)

app_name = "website"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('team/', TeamView.as_view(), name="team"),
    path('project/', ProjectListView.as_view(), name="projects"),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name="project"),
    path('about-us/', AboutUsView.as_view(), name="about-us"),
    path('contact-us/', ContactUsView.as_view(), name="contact-us"),

    path('enterprises/', ServicesEnterprisesView.as_view(), name="enterprises"),
    path('logistics/', ServicesLogisticsView.as_view(), name="logistics"),
    path('imports/', ServicesImportsView.as_view(), name="imports"),
    path('traders/', ServicesTradersView.as_view(), name="traders"),

]
