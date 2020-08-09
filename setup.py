import setuptools

with open("README.md",'r') as f:
    long_description = f.read()

setuptools.setup(
    name='hw-ctrl',
    version='0.0.1',
    description='Hardware controlling package for CircuitPython project'
    long_description = long_description,
    long_description_content_type="text/markdown",
    author="Cengizhan Oezmen",
    author_email="m.oezmen@cartelsol.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: Raspberry Pi OS :: 1.4"
    ],
    python_requires='>=3.7',
)
