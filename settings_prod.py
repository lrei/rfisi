# Django settings for rfisi project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Luis Rei', 'rifisi@mailinator.com'),
)

MANAGERS = ADMINS

#admin password is 'password'
DATABASES = {
    'default': {
        'ENGINE': 'mysql', #'postgresql_psycopg2', 'mysql', 'sqlite3'.
        'NAME': 'rfisi',      # Or path to database file if using sqlite3.
        'USER': 'martinhelder',                      # Not used with sqlite3.
        'PASSWORD': 'OdIUWXvaZGi_',                  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/admins3ig/rfisi/rfisi/files'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'



TEMPLATE_DIRS = (
'/home/admins3ig/rfisi/templates',
)


STATIC_DOC_ROOT = '/home/admins3ig/rfisi/rfisi/static'
FICHAS_DOC_ROOT = '/home/admins3ig/rfisi/files/tratamentos/fichas'
CV_DOC_ROOT = '/home/admins3ig/rfisi/files/candidaturas/cv'
BI_DOC_ROOT = '/home/admins3ig/rfisi/files/candidaturas/bi'



MY_SITE_URL = 'wardrop.fe.up.pt/martinhelder'
