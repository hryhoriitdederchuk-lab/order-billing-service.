DEFAULT_TAX_RATE = 0.20  # значення за замовчуванням, а не глобальна змінна, яку змінюють


class CustomerProfile:
    def __init__(self, user_id, email, password_hash, city, loyalty_points):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.city = city
        self.loyalty_points = loyalty_points


# Виправлення 2 (Stamp Coupling): приймаємо лише примітиви city і weight_kg,
# а не весь об'єкт CustomerProfile
def calculate_delivery_cost(city: str, weight_kg: float) -> float:
    base_rate = 80.0 if city == "Kyiv" else (50.0 if city == "Ivano-Frankivsk" else 110.0)
    return base_rate + (weight_kg * 15.0)


# Виправлення 1 (Common Coupling): ставка податку передається явно як аргумент
# (за замовчуванням 0.20), глобальної змінної більше немає.
# Виправлення 3 (Control Coupling): замість mode_flag є дві окремі функції.
def process_standard_invoice(amount: float, city: str, weight_kg: float,
                             tax_rate: float = DEFAULT_TAX_RATE) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = (amount * (1 + tax_rate)) + delivery
    return {"status": "PROCESSED", "total": round(total, 2)}


def process_tax_exempt_invoice(amount: float, city: str, weight_kg: float) -> dict:
    delivery = calculate_delivery_cost(city, weight_kg)
    total = amount + delivery
    return {"status": "TAX_EXEMPT", "total": round(total, 2)}
