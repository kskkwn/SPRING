import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spring-dtw",
    version="0.0.1",
    author="Keisuke Kawano",
    author_email="kskkwn@gmail.com",
    description="An implementation of the SPRING algorithm, which is a partial matching for time series with Dynamic Time Warping",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kskkwn/SPRING",
    packages=["spring"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
