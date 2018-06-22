from setuptools import find_packages, setup
import os

version = '1.0b3'
extras_require = {
    'test': 'bottle'
}
setup(
    name='openprocurement_client',
    version=version,
    description="Reference implementation of a client for OpenProcurement API.",
    long_description="{0}\n{1}".format(
        open("README.rst").read(),
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),

    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords='',

    author='',
    author_email='',
    url='https://github.com/ProzorroUKR/openprocurement.client.python',
    license='Apache Software License 2.0',

    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'gevent',
        'iso8601',
        'munch',
        'restkit',
        'retrying',
        'simplejson'
        # -*- Extra requirements: -*-
    ],
    tests_require=extras_require['test'],
    extras_require = extras_require,
    entry_points="""
    # -*- Entry points: -*-
    """,
    test_suite="openprocurement_client.tests"
)
