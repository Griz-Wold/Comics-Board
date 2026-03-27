from django.shortcuts import render, redirect
from .models import Posting
from .forms import PostingForm
from django.contrib.auth.decorators import login_required

def mainpage(request):
        postings = Posting.objects.select_related('account').all()
        return render(request, 'mainpage.html', {'postings': postings})

@login_required
def create_posting(request):
        if request.method=='POST':
                form = PostingForm(request.POST)
                if form.is_valid():
                        posting = form.save(commit=False)
                        posting.account = request.user
                        posting.save()
                        return redirect('account')
        else:
                form = PostingForm()
        return render(request, 'create_posting.html', {'form': form})