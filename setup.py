from setuptools import setup, find_packages

setup(
    name='weather_app',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    scripts=['weather_app_script.py'],  # Add this line
)
