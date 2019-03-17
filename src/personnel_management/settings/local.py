from personnel_management.settings.base import *


INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

# The Django Debug Toolbar will only be shown to these client IPs.
INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.33.1',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
    'HIDE_DJANGO_SQL': False,
}
GDAL_LIBRARY_PATH = 'C:\\OSGeo4W64\\bin\\gdal111.dll'
print(GDAL_LIBRARY_PATH)