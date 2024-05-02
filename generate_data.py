import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "electronics_vendor.settings")
django.setup()

from webapp.models import Product, Customer, Order, OrderItem
from django.utils.crypto import get_random_string
import random

def create_products():
    products = ['Camera', 'Laptop', 'Smartphone', 'Printer']
    for name in products:
        Product.objects.create(name=name, price=random.randint(100, 1000))

def create_customers():
    for _ in range(10):
        name = get_random_string()
        email = f"{name.lower()}@example.com"
        Customer.objects.create(name=name, email=email)

def create_orders():
    customers = Customer.objects.all()
    products = list(Product.objects.all())
    for customer in customers:
        order = Order.objects.create(customer=customer)
        for _ in range(random.randint(1, 5)):  # each customer orders 1-5 products
            OrderItem.objects.create(order=order, product=random.choice(products), quantity=random.randint(1, 3))

if __name__ == "__main__":
    create_products()
    create_customers()
    create_orders()

