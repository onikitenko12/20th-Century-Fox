from setuptools import setup, find_namespace_packages

setup(
    name='app_bot',
    version='2.0',
    description='App bot for iteraction with contact book',
    author='20th century fox team',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['runBot = app_bot.main:runBot']}
)