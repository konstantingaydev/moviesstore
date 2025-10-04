from django.shortcuts import render, redirect, get_object_or_404
from .models import Petition, Upvote
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    petitions = Petition.objects.all().order_by('-created_at')
    return render(request, 'petitions/index.html', {'petitions': petitions})

@login_required
def create(request):
    if request.method == 'POST' and request.POST['title'] != '' and request.POST['description'] != '':
        petition = Petition()
        petition.title = request.POST['title']
        petition.description = request.POST['description']
        petition.created_by = request.user
        petition.save()
        return redirect('petitions.index')
    else:
        return render(request, 'petitions/create.html')

@login_required
def upvote(request, id):
    petition = get_object_or_404(Petition, id=id)
    upvote, created = Upvote.objects.get_or_create(petition=petition, user=request.user)
    if created:
        petition.upvotes += 1
        petition.save()
    return redirect('petitions.index')