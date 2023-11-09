from setuptools import setup

setup(
    name='datascience_tools',
    version='0.1.0',
    packages=['datascience_tools', 'datascience_tools.ouliers'],
    package_dir={'': 'src'},
    url='https://github.com/ayaranitram/datascience_tools',
    license='MIT License',
    author='Martín Carlos Araya',
    author_email='martinaraya@gmail.com',
    description='A set of tools useful when processing data for machine learning projects.'
)
