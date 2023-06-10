import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='reqto',
    version='0.1.7',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='A wrapper around requests to tackle unstable timeout issues',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/reqto',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'eventlet','requests'
     ],
    python_requires='>=3.6',
)
    