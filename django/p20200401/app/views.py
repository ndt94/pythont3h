from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    pageSize = 10
    currentPage = int(request.GET.get('page', 1))
    keyword = request.GET.get('keyword', '')
    productList = Product.objects.filter(Q(name__contains=keyword) | Q(code__contains=keyword))
    paginator = Paginator(productList, pageSize)
    curItems = paginator.get_page(currentPage)
    pageNumber = [i for i in range(1, paginator.num_pages + 1)]
    offset = (currentPage - 1) * pageSize
    context = {'keyword': keyword, 'productList': productList, 'curItems': curItems, 'pageNumber': pageNumber, 'offset': offset}
    return render(request, 'index.html', context)