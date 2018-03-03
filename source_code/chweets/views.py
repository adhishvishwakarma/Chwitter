from django.shortcuts import render, get_object_or_404, redirect
from .forms import ChweetModelForm
from .models import Chweet


def view_chweets(request, chweet_id):
    chweet = get_object_or_404(Chweet, id=chweet_id)
    context = {'chweet': chweet}
    return render(request, "chweets/view_chweets.html", context)


def list_chweets(request):
    chweets = Chweet.objects.all().order_by("-timestamp")
    query = request.GET.get("q", None)
    if query is not None:
        chweets = chweets.filter(content__icontains=query)
    context = {'chweets': chweets}
    context['create_form'] = ChweetModelForm()
    if request.method == 'POST':
        form = ChweetModelForm(request.POST)
        if form.is_valid():
            chweet = form.save(commit=False)
            chweet.user = request.user
            chweet.save()
            return redirect('view', chweet.id)
    return render(request, "chweets/list_chweets.html", context)


def create_chweet(request):
    if request.method == 'POST':
        form = ChweetModelForm(request.POST)
        if form.is_valid():
            chweet = form.save(commit=False)
            chweet.user = request.user
            chweet.save()
            return redirect('view', chweet.id)
    else:
        form = ChweetModelForm
        return render(request, 'chweets/create_chweet.html', {'form': form})


def update_chweet(request, chweet_id):
    chweet = get_object_or_404(Chweet, id=chweet_id)
    if request.method == "POST":
        form = ChweetModelForm(request.POST, instance=chweet)
        if form.is_valid():
            chweet = form.save(commit=False)
            chweet.user = request.user
            chweet.save()
            return redirect('view', chweet.id)
    else:
        form = ChweetModelForm(initial={"content": chweet.content})
    return render(request, 'chweets/update_chweet.html', {'form': form})


def delete_chweet(request, chweet_id):
    chweet = get_object_or_404(Chweet, id=chweet_id)
    chweet.delete()
    return redirect('list')
