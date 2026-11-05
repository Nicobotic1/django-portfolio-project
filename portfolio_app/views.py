from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Portfolio, Student, Project


# Create your views here.

# Class-Based Views

# View for a student list that connects it to the student_list.html file.
class StudentListView(ListView):
    model = Student
    template_name = 'portfolio_app/student_list.html'
    context_object_name = 'students'

# View for a deatailed version of student information that connects to the student_detail.html file.
class StudentDetailView(DetailView):
    model = Student
    template_name = 'portfolio_app/student_detail.html'
    context_object_name = 'student'

# View for detailed portfolio information that connects to the portfolio_detail.html file. 
class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_app/portfolio_detail.html'
    context_object_name = 'portfolio'

    # I added this so I could change the url to use the student id instead of the portfolio id.
    # This makes it more organized and look nicer. It's safe because it is a one-to-one relationship.
    def get_object(self, queryset=None):
        return get_object_or_404(Portfolio, student_id=self.kwargs.get('student_id'))



# Function-Based Views

# View for the main page.
def index(request):
    # Retrieve active portfolio
    active_portfolios = Portfolio.objects.filter(
        is_active = True
    )

    return render(  request, 
                    'portfolio_app/index.html',
                    {'active_portfolios': active_portfolios}
                  )