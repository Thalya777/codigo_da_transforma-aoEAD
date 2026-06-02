from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "produtos/lista.html", {"produtos": produtos})

def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        descricao = request.POST["descricao"]
        preco = request.POST["preco"]
        quantidade = request.POST["quantidade"]
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
        return redirect("listar_produtos")
    return render(request, "produtos/cadastrar.html")

def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.nome = request.POST["nome"]
        produto.descricao = request.POST["descricao"]
        produto.preco = request.POST["preco"]
        produto.quantidade = request.POST["quantidade"]
        produto.save()
        return redirect("listar_produtos")
    return render(request, "produtos/atualizar.html", {"produto": produto})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect("listar_produtos")


from django.core.paginator import Paginator

def listar_produtos(request):
    busca = request.GET.get("busca")
    produtos = Produto.objects.all()
    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    paginator = Paginator(produtos, 5)  # 5 produtos por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "produtos/lista.html", {"page_obj": page_obj})

