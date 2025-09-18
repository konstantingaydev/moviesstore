from django.shortcuts import render
from movies.models import Review
# Create your views here.

# def home(request):
#     # This logic now lives in your home app's view
#     top_reviews = Review.objects.select_related('user', 'movie').order_by('-date')[:10]

#     # --- Add this line for debugging ---
#     print(top_reviews) 
#     # -----------------------------------

#     context = {
#         'top_reviews': top_reviews,
#     }
#     # Make sure it renders your index.html template
#     return render(request, 'index.html', context)

# def index(request):
#     template_data = {}
#     template_data['title'] = 'Movies Store'
#     return render(request, 'home/index.html', {'template_data': template_data})
def home(request):
    # Data from your old 'index' view
    template_data = {}
    template_data['title'] = 'Movies Store'
    
    # Data for the reviews
    top_reviews = Review.objects.select_related('user', 'movie').order_by('-date')[:10]
    
    # Combine everything into one context dictionary
    context = {
        'template_data': template_data,
        'top_reviews': top_reviews,
    }
    
    return render(request, 'home/index.html', context)

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})
