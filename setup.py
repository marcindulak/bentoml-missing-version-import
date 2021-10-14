import setuptools

exec(open('mypackage/_version.py').read())

setuptools.setup(
    name='mypackage',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'bentoml',
        'scikit-learn',
    ],
)
