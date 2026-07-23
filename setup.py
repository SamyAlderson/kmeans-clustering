from setuptools import setup

def read_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

setup(
    name='kmeans-clustering',
    version='1.0',
    description='A basic implementation of K-means clustering in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/samyalderson/kmeans-clustering',
    author='Samy Alderson',
    author_email='samyalderson@example.com',
    license='MIT',
    packages=['kmeans_clustering'],
    install_requires=read_requirements(),
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ]
)