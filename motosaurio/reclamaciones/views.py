from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reclamacion
from .forms import ReclamacionForm

@login_required
def register(request):
    if request.method == 'POST':
        form = ReclamacionForm(request.POST)
        if form.is_valid():
            new_reclamacion = form.save(commit=False)
            new_reclamacion.username = request.user.username
            new_reclamacion.save()
            return render(request,
                        'reclamaciones/done.html',
                        {'user': request.user})
    else:
        form = ReclamacionForm()
    return render(request,
                'reclamaciones/register.html',
                {'form': form})
