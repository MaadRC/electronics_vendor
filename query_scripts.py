import django
django.setup()

from webapp.models import Customer, OrderItem

def top_spending_customer():
    return Customer.objects.annotate(total_spent=Sum('order__orderitem__total_price')).order_by('-total_spent').first()

def top_selling_products():
    return OrderItem.objects.values('product__name').annotate(total_sold=Sum('quantity')).order_by('-total_sold')[:2]

if __name__ == "__main__":
    print("Top Spending Customer:", top_spending_customer())
    print("Top Selling Products:", top_selling_products())

