import os

from django.conf import settings
from wagtail.contrib.redirects.models import Redirect


def write_redirects_to_netlify_file(filename="_redirects"):
    """
    Write redirects from Wagtail to a Netlify-formatted ``_redirects`` file.
    """
    redirects_filename = os.path.join(settings.BUILD_DIR, filename)
    redirect_lines = generate_redirect_lines()

    with open(redirects_filename, "w") as outfile:
        outfile.write("\n".join(redirect_lines))


def generate_redirect_lines():
    """
    Generate a list of strings representing redirects accroding to the Netlify format.

    The redirect format is defined here: https://docs.netlify.com/routing/redirects/

    Example::

        # Redirects from what the browser requests to what we serve
        /home              /                                    302
        /blog/my-post.php  /blog/my-post                        301
        /news              /blog                                302
        /cuties            https://www.petsofnetlify.com        302
    """
    redirects = []

    for redirect in Redirect.objects.all():
        status_code = "302"
        if redirect.is_permanent:
            status_code = "301"

        redirect_line = f"{redirect.old_path}\t{redirect.link}\t{status_code}"
        print(f"Adding line: {redirect_line}")

        redirects.append(redirect_line)
    return redirects
