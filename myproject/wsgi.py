"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# Get the default WSGI application
application = get_wsgi_application()

# Wrap the application to add custom headers
def custom_wsgi_application(environ, start_response):
    # Add the nosniff header to the response
    def custom_start_response(status, headers, exc_info=None):
        headers.append(('X-Content-Type-Options', 'nosniff'))
        return start_response(status, headers, exc_info)

    # Call the original application
    return application(environ, custom_start_response)