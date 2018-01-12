from setuptools import setup

with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='pipsi',
    version='0.10.dev',
    description='Wraps pip and virtualenv to install scripts',
    long_description=readme,
    license='BSD',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    url='http://github.com/mitsuhiko/pipsi/',
    packages=['pipsi'],
    package_data={
        'pipsi': ['scripts/*.py'],
    },
    include_package_data=True,
    install_requires=[
        'Click',
        'virtualenv;python_version<"3.0"',
    ],
    entry_points='''
    [console_scripts]
    pipsi=pipsi:cli
    '''
)
