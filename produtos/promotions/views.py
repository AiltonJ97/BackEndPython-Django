from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

def produto_new(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()          # salva no banco de dados
            return redirect('produto_list')   # redirecione para alguma página lista
    else:
        form = ProdutoForm()

    return render(request, 'produto_form.html', {'form': form})


def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produto_list.html', {'produtos': produtos})
