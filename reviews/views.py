from django.views.generic import CreateView
from .models import Review
from django.urls import reverse_lazy

class ReviewCreateView(CreateView):
    model = Review
    fields = ['text', 'rating']
    template_name = 'reviews/review_form.html'

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['product_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_detail', args=[self.kwargs['product_id']])