
import codecs
import os

from distutils.core import setup


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts),
                       encoding='utf8').read()

setup(
    name='django-conversejs',
    description='Adds converse.js (javascript XMPP client) to Django',
    version='0.1',
    long_description=read('README.rst'),
    packages=['conversejs'],
    author='Sergio Oliveira',
    author_email='sergio@tracy.com.br',
    url='https://github.com/TracyWebTech/django-conversejs',
    license='MPL v2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
)