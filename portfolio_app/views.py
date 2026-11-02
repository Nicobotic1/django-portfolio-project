from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Portfolio, Student


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