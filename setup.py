import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ptsne-pytorch",
    version="0.0.1",
    author="Andreas Hinterreiter",
    author_email="andreas.hinterreiter@jku.at",
    description="PyTorch reimplementation of parametric t-SNE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/einbandi/project_name",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        
        "License :: OSI Approved :: MIT License",
        
        "Operating System :: OS Independent",
    ],
)