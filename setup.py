from setuptools import setup
setup(
    name="basiqrapid",
    packages=["basiqrapid"],
    version="1.0.2",
    description="A Python wrapper for Basiq.io’s API",
    author="Michael Gee",
    python_requires=">=3",
    install_requires=["requests","pandas"],
    author_email="michael.gee2018@gmail.com",
    url="https://github.com/mike-gee/basiqrapid",
    download_url="https://github.com/mike-gee/basiqrapid/archive/v_01.tar.gz",
    keywords=["basiq", "finance", "sdk", "api", "python", "wrapper"],
    classifiers=[]
)