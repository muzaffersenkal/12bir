from django.views.generic import ListView , TemplateView,DetailView,FormView
from .models import Field
from django.db.models import Avg
from .forms import ReviewModelForm


class IndexView(TemplateView):

    template_name = "index.html"


class ListView(ListView):

    queryset =  Field.objects.all()
    print(queryset)
    template_name ="pitch_list.html"



class DetailView(DetailView,FormView):

    model = Field
    template_name = "pitch_detail.html"
    form_class = ReviewModelForm

    def get_object(self):
        slug = self.kwargs.get("slug")
        return Field.objects.get(slug=slug)

    def get_context_data(self, *args,**kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        # Add in a QuerySet of all the books
        avg =  self.get_object().review.aggregate(Avg('rating'))
        context['rate'] = avg["rating__avg"]
        return context

    def form_valid(self, form):
        contact_name = self.form.cleaned_data['contact_name']

        return super(DetailView, self).form_valid(form)





