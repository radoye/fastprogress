import setuptools

# note: version is maintained inside fastprogress/version.py
exec(open('fp/version.py').read())

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "fp",
    version = __version__,
    author = "Sylvain Gugger",
    license = "Apache License 2.0",
    description = "A nested progress with plotting options for fastai",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/radoye/fastprogress",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3.6",
        'Programming Language :: Python :: 3.7',
    ],
    setup_requires = ['pytest-runner'],
    tests_require = ['pytest'],
    test_suite = 'tests',
)
