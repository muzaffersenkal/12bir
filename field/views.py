from django.views.generic import ListView , TemplateView,DetailView
from .models import Field

class IndexView(TemplateView):

    template_name = "index.html"


class ListView(ListView):
    queryset =  Field.objects.all()
    print(queryset)
    template_name ="pitch_list.html"



class DetailView(DetailView):
    model = Field
    template_name = "pitch_detail.html"

    def get_object(self):
        slug = self.kwargs.get("slug")
        return Field.objects.get(slug=slug)






