# Este arquivo conterá a configuração do pacote.
from setuptools import setup, find_packages

setup(
    name="cafeteria_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "pandas",
    ],
)
