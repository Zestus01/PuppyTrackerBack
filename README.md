# Django Template
## Setup
After creating your project, some additional configuration is required to allow the project to run in Gitpod.

1. Install the [`django-cors-headers`](https://pypi.org/project/django-cors-headers/) package and follow the Setup instructions in the README.

1. Add the following to the project's `settings.py`:
    ```
    CSRF_TRUSTED_ORIGINS = ['https://*.gitpod.io']
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]
    ```