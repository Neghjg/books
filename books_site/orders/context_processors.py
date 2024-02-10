from orders.models import Order


def get_user_orders(request):
    if request.user.is_authenticated:
        orders_users = Order.objects.filter(user=request.user).prefetch_related("items").only("user", "id", "items", "status", "created")
        return {"orders_users": orders_users}
    else:
        return {"order_users": None}