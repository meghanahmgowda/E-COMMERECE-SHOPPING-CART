from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Display all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# Show product details
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

# View shopping cart
def cart(request):
    cart_items = request.session.get('cart', {})
    items = []
    total = 0
    for key, item in cart_items.items():
        subtotal = item['price'] * item['quantity']
        total += subtotal
        items.append({'key': key, **item, 'subtotal': subtotal})
    tax = total * 0.05
    grand_total = total + tax
    return render(request, 'store/cart.html', {
        'cart_items': items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total
    })

# Add product to cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    qty = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})
    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += qty
    else:
        cart[str(product.id)] = {'name': product.name, 'price': float(product.price), 'quantity': qty}
    request.session['cart'] = cart
    return redirect('cart')

# Remove product from cart
def remove_from_cart(request, key):
    cart = request.session.get('cart', {})
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
    return redirect('cart')

# Checkout
def checkout(request):
    cart_items = request.session.get('cart', {})
    items = []
    total = 0
    for key, item in cart_items.items():
        subtotal = item['price'] * item['quantity']
        total += subtotal
        items.append({'key': key, **item, 'subtotal': subtotal})
    tax = total * 0.05
    grand_total = total + tax
    if request.method == 'POST':
        request.session['cart'] = {}  # Clear cart after checkout
        return render(request, 'store/checkout_success.html', {'grand_total': grand_total})
    return render(request, 'store/checkout.html', {
        'cart_items': items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total
    })
