from genericpath import exists
from bakery.management.commands import build

import os

from fs import path
from fs import copy
from django.core.files.storage import default_storage

from django.conf import settings
from wagtail.documents import get_document_model


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

        Document = get_document_model()
        target_dir = path.join(self.fs_name, self.build_dir, settings.MEDIA_URL.lstrip('/'))

        # Documents managed by Wagtail are handled differently when exposed. We need to make
        # sure that we creating the correct structure in the /media/ folder for documents.
        for doc in Document.objects.all():
            filename = f"{target_dir}/{doc.url}"
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename), exist_ok=True)

            with doc.file.open("rb") as infile:
                with open(f"{target_dir}/{doc.url}", "wb") as outfile:
                    outfile.write(infile.read())


        for obj in bucket.objects.all():
            print(obj.key)

            target_dir = path.join(self.fs_name, self.build_dir, settings.MEDIA_URL.lstrip('/'))
            obj_dir = path.join(target_dir, os.path.dirname(obj.key))

            if not os.path.exists(obj_dir):
                os.makedirs(obj_dir, exist_ok=True)

            s3_file = default_storage.connection.Object(obj.bucket_name, obj.key)

            print(f"Downloading file from {target_dir}/{obj.key}")
            s3_file.download_file(f"{target_dir}/{obj.key}")