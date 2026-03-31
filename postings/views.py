from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting
from .forms import PostingForm
from django.contrib.auth.decorators import login_required

def mainpage(request):
        postings = Posting.objects.select_related('account').all()
        return render(request, 'mainpage.html', {'postings': postings})

@login_required
def create_posting(request):
        if request.method=='POST':
                form = PostingForm(request.POST, request.FILES)
                if form.is_valid():
                        posting = form.save(commit=False)
                        posting.account = request.user
                        posting.save()
                        return redirect('account')
        else:
                form = PostingForm()
        return render(request, 'create_posting.html', {'form': form})

def posting_detail(request, id):
        posting = get_object_or_404(Posting, pk=id)
        return render(request, 'posting_detail.html', {'posting': posting})

def delete_posting(request, id):
        posting = Posting.objects.get(pk=id)
        if request.user == posting.account:
                if request.method == 'POST':
                        posting.delete()
                        return redirect('account')
        else:
                return redirect('mainpage')
        return render(request, 'delete_posting.html', {'posting': posting})

def edit_posting(request, id):
        posting = Posting.objects.get(pk=id)
        if request.user == posting.account:
                if request.method == 'POST':
                        form = PostingForm(request.POST, request.FILES, instance=posting)
                        if form.is_valid():
                                form.save()
                                return redirect('posting_detail', id=posting.id)
                else:
                        form = PostingForm(instance=posting)
        else:
                return redirect('mainpage')
        return render(request, 'edit_posting.html', {'form': form, 'posting': posting})
