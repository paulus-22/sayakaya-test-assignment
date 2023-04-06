import datetime
import string

# suppose import user from model
from app.model import User, PromoCode


def fetchUsers(user_id):
    today = datetime.date.today().date()
    user = User.objects.get(user_id=user_id)
    if (
        user.date_of_birth.month == current_date.month
        and user.date_of_birth.day == current_date.day
    ):
        user.is_verified = True
        user.save()


def generatePromoCode():
    promo_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    discount = 0.25  # 25% discount for Sayakaya products
    validity_date = datetime.date.today()
    promo = PromoCode(code=promo_code, discount=discount, validity_date=validity_date)
    promo.save()
    return promo_code


def sendNotification():
    current_date = datetime.date.today()
    users = User.objects.filter(
        date_of_birth__month=current_date.month,
        date_of_birth__day=current_date.day,
        is_verified=True,
    )
    for user in users:
        promo_code = generatePromoCode()
        message = f"Happy Birthday {user.name}! As a special gift, use promo code {promo_code} to get 10% off on Sayakaya products today."
        # send email
        send_email(user.email, "Happy Birthday!", message)
        # or send whatsapp
        send_whatsapp(user.phone_number, message)
