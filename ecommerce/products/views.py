from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from .models import Product,Category
# Create your views here.



def ProductListView(request):
    ProductList= Product.objects.all()
    context = {
        "ProductList":ProductList
    }
    template_name = "productlist.html"

    return render(request,template_name,context)


    # def get_querset(self,*args,**kwargs):
    #     qs = super(ProductListView,self).get_queryset(*args,**kwargs)
    #     query = self.request.POST.get('q')
    #     if query:



def ProductDetailView(request,id):
    product = get_object_or_404(Product,id=id)
    context = {
        "product":product
    }
    template_name = "productdetail.html"
    return render(request,template_name,context)


def CategoryListview(request):
    CategoryList = Category.objects.all
    context = {
        "CategoryList":CategoryList
    }
    template_name = "categorylistview.html"
    return render(request,template_name,context)


def CategoryDetail(request,id):
    category = get_object_or_404(Category,id=id)
    product = Product.objects.filter(category=category)
    context = {
        "category":category,
        "product":product
    }
    template_name = "category-detail.html"
    return render(request,template_name,context)