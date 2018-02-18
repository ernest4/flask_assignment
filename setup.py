from setuptools import setup, find_packages

setup(
    name='flaskSysInfo',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    entry_points={'console_scripts':['comp30670_flaskSysInfo=app.run']}
)
