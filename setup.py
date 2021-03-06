#encoding: utf-8

from setuptools import setup, find_packages

from thjodskra import get_version

setup(
    name = "django-thjodskra",
    version = get_version(),
    description = "django-thjodskra is a simple app for integrating the icelandic national registry into your django project",
    author = "Úlfur Kristjánsson",
    author_email = "ulfur@theawesometastic.com",
    url = "https://github.com/ulfur/django-thjodskra",
    packages = find_packages( ),
    include_package_data=True
)
