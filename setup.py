from setuptools import setup
REQUIRES = [
    'records',
    'allure',
    'structlog'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/widowblack11/db_client.git',
    license='MIT',
    author='oksanaprokopenko',
    author_email='-',
    istall_requires=REQUIRES,
    description='db client with sql'
)
