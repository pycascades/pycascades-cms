from genericpath import exists
from bakery.management.commands import build

import os

from fs import path
from fs import copy
from django.core.files import storage 
from django.core.files.storage import get_storage_class, default_storage

from django.conf import settings
from wagtail.documents import get_document_model


class Command(build.Command):

    def handle(self, *args, **options):
        """
        Making it happen.
        """
        build.logger.info("Build started")

        # Set options
        self.set_options(*args, **options)

        # Get the build directory ready
        if not options.get("keep_build_dir"):
            self.init_build_dir()

        # Build up static files
        if not options.get("skip_static"):
            self.build_static()

        # Build the media directory
        if not options.get("skip_media"):
            self.build_media()

        old_media_root = settings.MEDIA_ROOT
        old_storage = storage.default_storage

        settings.MEDIA_ROOT = f"{self.build_dir}/{self.media_root}"
        storage.default_storage = get_storage_class('django.core.files.storage.FileSystemStorage')

        # Build views
        self.build_views()

        settings.MEDIA_ROOT = old_media_root
        storage.default_storage = old_storage

        # Close out
        build.logger.info("Build finished")

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


        #for obj in bucket.objects.all():
        #    print(obj.key)

        #    target_dir = path.join(self.fs_name, self.build_dir, settings.MEDIA_URL.lstrip('/'))
        #    obj_dir = path.join(target_dir, os.path.dirname(obj.key))

        #    if not os.path.exists(obj_dir):
        #        os.makedirs(obj_dir, exist_ok=True)

        #    s3_file = default_storage.connection.Object(obj.bucket_name, obj.key)

        #    print(f"Downloading file from {target_dir}/{obj.key}")
        #    s3_file.download_file(f"{target_dir}/{obj.key}")