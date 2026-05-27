from django.shortcuts import render, redirect
from .models import Product,Cart

# Create your views here.
def add_product(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')

        stock = request.POST.get('stock')
        category = request.POST.get('category')

        Product.objects.create(id=id, p_name=name, p_price=price, p_quantity = stock,p_type=category)
        return redirect("view")
    return render(request,"product.html")




def view_all_products(request):
    data=Product.objects.all().values()

    return render(request,"product list.html",{
        "product_data":list(data)
    })




def delete_by_id(request, id):
    if request.method == 'POST':
        data=Product.objects.get(id=id)
        data.delete()
        return redirect('http://127.0.0.1:8000/user/view_all_products/')
    return render(request,"product list.html")

def add_to_cart(request, id):

    if request.method == 'POST':

        prod= Product.objects.get(id=id)
        id=prod.id
        name=prod.p_name
        price=prod.p_price
        Cart.objects.create(prod_id=id,prod_name=name,prod_price=price)
        return render(request,"cartproduct.html")



