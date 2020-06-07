from setuptools import find_packages, setup

requirements = [
    'fastapi>=0.55.1',
    'environs'
]

develop_requirements = [
    'coverage',
    'autopep8',
    'flake8',
    'mypy',
    'autoflake',
    'isort',
    'black',
    'pytest',
]

uvicorn_requirements = [
    'uvicorn'
]

extras_require = {
    'dev': develop_requirements,
    'uvicorn': uvicorn_requirements,
}


setup(
    name='fastapi_preset',
    version='0.1.0',
    description='fastapi preset',
    author='cln-m4rie',
    author_email='',
    url='https://github.com/cln-m4rie/fastapi_preset',
    install_requires=requirements,
    extras_require=extras_require,
    packages=find_packages(exclude=[])
)
