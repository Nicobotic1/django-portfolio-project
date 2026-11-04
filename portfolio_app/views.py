from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Portfolio, Student, Project


# Create your views here.

# Class-Based Views
class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'

    def get_object(self, queryset=None):
        # Absolutely safe because user_id is guaranteed unique in this table
        return get_object_or_404(Portfolio, student_id=self.kwargs.get('student_id'))



# Function-Based Views
def index(request):
    # Retrieve active portfolio
    active_portfolios = Portfolio.objects.filter(
        is_active = True
    )

    return render(  request, 
                    'portfolio_app/index.html',
                    {'active_portfolios': active_portfolios}
                  )