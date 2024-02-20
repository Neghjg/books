


def requires_delivery(delivary, address):
    if delivary == '0':
        return "самовывоз"
    elif address != None:
        return f"доставка на {address} "
    
def payment_on_get(pay):
    if pay == '1':
        return 'оплата при получении'