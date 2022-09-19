from django.views.generic.list import ListView

from app.models import Task


class AppListView(ListView):
    model = Task
    paginate_by = 10
    template_name = "app/list.html"
