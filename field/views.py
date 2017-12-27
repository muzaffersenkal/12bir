from django.views.generic import ListView , TemplateView,DetailView,FormView
from django.views.generic.edit import CreateView
from .models import Field
from django.db.models import Avg
from .forms import ReviewModelForm
from django.urls import reverse_lazy

class IndexView(TemplateView):

    template_name = "index.html"


class ListView(ListView):

    queryset =  Field.objects.all()
    print(queryset)
    template_name ="pitch_list.html"



class DetailView(DetailView,FormView,CreateView):

    model = Field
    template_name = "pitch_detail.html"
    form_class = ReviewModelForm

    def get_success_url(self,  **kwargs):

            return reverse_lazy('detail',  kwargs={'slug':self.get_object().slug})

    def get_object(self):
        slug = self.kwargs.get("slug")
        return Field.objects.get(slug=slug)

    def get_context_data(self, *args,**kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        # Add in a QuerySet of all the books
        avg =  self.get_object().review.aggregate(Avg('rating'))
        context['rate'] = avg["rating__avg"]
        context['comment_list']= self.get_object().review.all()
        return context

    def form_valid(self, form):
        print(form)
        review = form.save(commit=False)
        review.post = self.get_object()
        review.rating=form.cleaned_data['rating']
        review.save()
        return super(DetailView, self).form_valid(form)









