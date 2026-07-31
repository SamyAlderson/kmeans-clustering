from setuptools import setup, find_packages

setup(
    name='kmeans-clustering',
    version='1.1',  # bumped version
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='General kmeans clustering library',
    url='https://github.com/SamyAlderson/kmeans-clustering',
    author='Samy Alderson',
    author_email='samyalder@domain.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='kmeans clustering',
    python_requires='>=3.7',  # specify minimum python version
    install_requires=[],  # add any dependencies here
    extras_require={
        'dev': ['pytest', 'flake8'],  # dev dependencies
    },
)