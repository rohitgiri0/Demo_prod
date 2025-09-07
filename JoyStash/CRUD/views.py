from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Snippet
from .forms import SnippetForm


@login_required
def snippet_list(request):
    """
    List all snippets for the logged-in user.
    """
    snippets = Snippet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'CRUD/home.html', {'snippets': snippets})

@login_required
def toggle_favorite(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    snippet.is_favorite = not snippet.is_favorite
    snippet.save()
    return redirect('home')

@login_required
def snippet_detail(request, pk):
    """
    Show details of a single snippet.
    """
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    return render(request, 'CRUD/snippet_detail.html', {'snippet': snippet})


@login_required
def snippet_update(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SnippetForm(instance=snippet)  # pre-populate form with existing data

    return render(request, 'CRUD/snippet_form.html', {'form': form, 'snippet': snippet})


@login_required
def snippet_delete(request, pk):
    """
    Delete a snippet.
    """
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    if request.method == 'POST':
        snippet.delete()
        return redirect('snippet_list')
    return render(request, 'CRUD/snippet_confirm_delete.html', {'snippet': snippet})

@login_required
def snippet_create(request):
    """
    Create a new snippet.
    """
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SnippetForm()
    return render(request, 'CRUD/snippet_form.html', {'form': form})