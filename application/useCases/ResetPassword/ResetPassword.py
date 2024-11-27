import os
from app.models import CustomUser
from django.core.mail import send_mail
import random
import string

from .protocols.ResetPasswordRequest import ResetPasswordRequest


class ResetPassword:
    def execute(self, inbound: ResetPasswordRequest) -> bool:
        user = CustomUser.objects.get(email=inbound.email)
        temp_password = "".join(
            random.choices(string.ascii_letters + string.digits, k=8)
        )
        user.set_password(temp_password)
        user.save()

        send_mail(
            "Password Reset Request",
            f"Your temporary password is: {temp_password}\nPlease change your password after logging in.",
            os.getenv("EMAIL_HOST_USER"),
            [inbound.email],
            fail_silently=False,
        )

        return True
