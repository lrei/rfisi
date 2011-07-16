# Django settings for rfisi project.

DEBUG = True
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
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/Users/rei/FEUP/LSDO/rfisi/files'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

TEMPLATE_DIRS = (
'/Users/rei/FEUP/LSDO/rfisi/templates',
)

STATIC_DOC_ROOT = '/Users/rei/FEUP/LSDO/rfisi/static'
FICHAS_DOC_ROOT = '/Users/rei/FEUP/LSDO/rfisi/files/tratamentos/fichas'
CV_DOC_ROOT = '/Users/rei/FEUP/LSDO/rfisi/files/candidaturas/cv'
BI_DOC_ROOT = '/Users/rei/FEUP/LSDO/rfisi/files/candidaturas/bi'

SITE_URL = 'wardrop.fe.up.pt/martinhelder'
MY_SITE_URL = 'rfisi.com'

LOGIN_URL = '/utilizadores/login/'
LOGOUT_URL = '/utilizadores/logout/'
LOGIN_REDIRECT_URL = '/'
