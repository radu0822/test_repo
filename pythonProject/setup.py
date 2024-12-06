from setuptools import setup, find_packages


setup(
    name="airflow-plugin-github",
    version="1.0.0",
    packages=find_packages(),
    install_requires=['apache-airflow>=2.0', 'requests'],
    entry_points={
        'airflow.plugins': ['github_plugin = github_plugin.plugin:GitHubPlugin']
        },
)