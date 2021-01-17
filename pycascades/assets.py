from django_assets import Bundle, register


register(
    "pycascades.css",
    Bundle(
        "css/skeleton/normalize.css",
        "css/skeleton/skeleton.css",
        "css/misc/ff.common.css",
        "css/pycascades/pycascades.css",
        "css/pycascades/pycascades.tito.css",
        "css/pycascades/pycascades.content.css",
        "css/pycascades/pycascades.home.css",
        "css/pycascades/pycascades.news.css",
        "css/pycascades/pycascades.about.css",
        "css/pycascades/pycascades.venue.css",
        "css/pycascades/pycascades.tickets.css",
        "css/pycascades/pycascades.schedule.css",
        "css/pycascades/pycascades.speakers.css",
        "css/pycascades/pycascades.sponsors.css",
        "css/pycascades/pycascades.talks.css",
        filters="cssmin",
        output="css/min/pycascades.%(version)s.css",
    ),
)

register(
    "pycascades.js",
    Bundle(
        "js/misc/modernizr.js",
        "js/angular/angular.js",
        "js/angular/angular-animate.js",
        "js/misc/angular-scroll.js",
        "js/misc/angular-parallax.js",
        "js/headroom/headroom.js",
        "js/misc/instafeed.js",
        "js/misc/ff.imghelpers.js",
        "js/pycascades/pycascades.js",
        filters="jsmin",
        output="js/min/pycascades.%(version)s.js",
    ),
)
