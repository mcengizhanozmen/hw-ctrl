import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='hil',
    version='0.0.2',
    description='Hardware controlling module of HIL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Cengizhan Oezmen',
    author_email="m.oezmen@cartelsol.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
