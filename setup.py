import setuptools

from glob import glob
from os.path import basename
from os.path import splitext


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setuptools.setup(
    name="spring-dtw",
    version="0.0.1",
    description="An implementation of the SPRING algorithm, which is a partial matching for time series with Dynamic Time Warping",
    author="Keisuke Kawano",
    url="https://github.com/kskkwn/SPRING",
    packages=setuptools.find_packages("spring"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('spring/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
)
