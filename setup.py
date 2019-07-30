import setuptools

with open("Pypi.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='serial-j',
    version='1.0.8',
    author='Junpu Fan',
    author_email='junpufan@me.com ',
    description='Validating and Serializing JSON data into Python object with minimal effort.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/JunpuFan/serial-j',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
