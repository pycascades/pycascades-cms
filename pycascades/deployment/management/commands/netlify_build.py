import os

from bakery.management.commands import build
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.management.base import CommandError
from fs import path
from wagtail.documents import get_document_model

from ...redirects import write_redirects_to_netlify_file


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

        self.build_redirects()

        # Build views
        self.build_views()

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
            print("S3 storage unavailable, deferring to default bakery storage")
            super().build_media()
            return

        Document = get_document_model()
        target_dir = path.join(self.fs_name, self.build_dir)

        # Documents managed by Wagtail are handled differently when exposed. We need to
        # make sure that we are creating the correct structure in the /media/
        # folder for documents.
        for doc in Document.objects.all():
            filename = f"{target_dir}/{doc.url}"
            if not os.path.exists(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename), exist_ok=True)

            with doc.file.open("rb") as infile:
                with open(f"{target_dir}/{doc.url}", "wb") as outfile:
                    outfile.write(infile.read())

        for obj in bucket.objects.all():
            print(obj.key)

            target_dir = path.join(
                self.fs_name, self.build_dir, settings.MEDIA_URL.lstrip("/")
            )
            obj_dir = path.join(target_dir, os.path.dirname(obj.key))

            if not os.path.exists(obj_dir):
                os.makedirs(obj_dir, exist_ok=True)

            s3_file = default_storage.connection.Object(obj.bucket_name, obj.key)

            print(f"Downloading file from {target_dir}/{obj.key}")
            s3_file.download_file(f"{target_dir}/{obj.key}")

    def build_redirects(self):
        """Redirects are configured in a file called '_redirects'
        at the root of the build directory
        """
        if not hasattr(settings, "BUILD_DIR"):
            raise CommandError("BUILD_DIR is not defined in settings")

        write_redirects_to_netlify_file()
