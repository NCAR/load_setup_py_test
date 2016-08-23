import setuptools
import numpy.distutils.core
 

ext1 = numpy.distutils.core.Extension(
    name = "fortest._fortest",
    sources = ["fortran/fortest.f90",
               "fortran/fortest.pyf"]
    )

with open("src/fortest/version.py") as f: 
    exec(f.read())

requirements = [
    "numpy>=1.9.0",
    ] 

numpy.distutils.core.setup( 
    author = "Bill Ladwig",
    author_email = "ladwig@ucar.edu",
    description = "Test case for conda-build crash",
    url = "https://github.com/NCAR/load_setup_py_test",
    install_requires = requirements,
    name = "fortest",
    version =  __version__,
    packages = setuptools.find_packages("src"),
    ext_modules = [ext1],
    package_dir = {"" : "src"},
    scripts=[]
)  
