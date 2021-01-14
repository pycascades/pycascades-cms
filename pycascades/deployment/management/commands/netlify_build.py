from genericpath import exists
from bakery.management.commands import build

import os

from fs import path
from fs import copy
from django.core.files.storage import default_storage
from django.utils.encoding import smart_text

from django.conf import settings


class Command(build.Command):

    def build_media(self):
        """
        Build the media files.
        """
        build.logger.debug("Building media directory")
        if self.verbosity > 1:
            self.stdout.write("Building media directory")


        try:
            bucket = default_storage.bucket
        except AttributeError:
            print("this is not an S3 storage")
            super().build_media()
            return


        for obj in bucket.objects.all():
            print(obj.key)

            target_dir = path.join(self.fs_name, self.build_dir, settings.MEDIA_URL.lstrip('/'))
            obj_dir = path.join(target_dir, os.path.dirname(obj.key))

            if not os.path.exists(obj_dir):
                os.makedirs(obj_dir, exist_ok=True)

            s3_file = default_storage.connection.Object(obj.bucket_name, obj.key)

            print(f"Downloading file from {target_dir}/{obj.key}")
            s3_file.download_file(f"{target_dir}/{obj.key}")