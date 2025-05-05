import os
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from app.models import CustomUser


class UpdateProfilePicture:
    def execute(user: CustomUser, profile_picture):

        user_id = user.id

        timestamp = datetime.now().strftime("%H%M%S")

        file_extension = os.path.splitext(profile_picture.name)[-1]

        new_file_name = f"{user_id}-{timestamp}{file_extension}"

        file_path = f"profile_pictures/{new_file_name}"
        saved_path = default_storage.save(
            file_path, ContentFile(profile_picture.read())
        )

        user.profile_picture.name = saved_path
        user.save()
        return user
