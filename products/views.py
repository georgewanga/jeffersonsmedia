from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from jeffersonsmedia.forms import AddItemForm
from carts.models import Cart
from products.models import Product

class ProductListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.newOrGet(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not found..')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        return instance
    

class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = 'products/featured-detail.html'
    
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     return Product.objects.featured()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset,
    }
    content_type = None
    return render(request, 'products/list.html',context,content_type)


class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    
    def get_context_data(self,*args,**kwargs):
        context=super(ProductListView,self).get_context_data(*args,**kwargs)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('Product does not exist')
        return instance
    
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None,*args,**kwargs):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404('Product does not exist')
    context = {
        'object':instance,
    }
    content_type = None
    return render(request, 'products/detail.html',context,content_type)

def home(request):
    context = {
        'page_title':'Products'
    }
    content_type = None
    return render(request, 'products/home.html',context,content_type)


def addProduct(request):
    form = AddItemForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        'page_title':'Add Item',
        'form': form
    }
    content_type = None
    return render(request, 'products/add_item.html',context,content_type)