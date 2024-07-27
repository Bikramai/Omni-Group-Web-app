from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from src.administration.admins.filters import PropertyFilter
from src.administration.admins.models import Property, PropertyTag

import folium


class HomeView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['projects'] = Property.objects.all()
        return context


class TeamView(TemplateView):
    template_name = 'website/team.html'


class ContactUsView(TemplateView):
    template_name = 'website/contact-us.html'


class AboutUsView(TemplateView):
    template_name = 'website/about-us.html'


class ProjectListView(ListView):
    queryset = Property.objects.all().values_list(
            'id', 'name', 'price_start', 'price_end', 'property_id', 'property_type'
        )
    template_name = 'website/projects.html'
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        _filter = PropertyFilter(self.request.GET, queryset=Property.objects.filter())
        context['filter_form'] = _filter.form

        paginator = Paginator(_filter.qs, 50)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context['object_list'] = page_object
        return context


class ProjectDetailView(DetailView):
    template_name = 'website/project.html'
    model = Property

    def get_object(self, queryset=None):
        return get_object_or_404(Property, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['projects'] = Property.objects.all().order_by('?')[0:9]
        context['tags'] = PropertyTag.objects.all()

        property_object = self.get_object()
        if property_object.lat and property_object.long:
            marks = folium.Map(location=[property_object.lat, property_object.long], zoom_start=6)
            co_ordinates = (property_object.lat, property_object.long)
            folium.Marker(co_ordinates, popup=str(property_object.name)).add_to(marks)
            context['map'] = marks._repr_html_()
        else:
            context['map'] = None

        return context


class ServicesEnterprisesView(TemplateView):
    template_name = 'website/service_enterprise.html'


class ServicesImportsView(TemplateView):
    template_name = 'website/service_imports.html'


class ServicesTradersView(TemplateView):
    template_name = 'website/service_traders.html'


class ServicesLogisticsView(TemplateView):
    template_name = 'website/service_logistics.html'


