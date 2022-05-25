from setuptools import setup
from setuptools import find_packages

VERSION = "0.3.0"


# read the contents of your README file
def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="webcron",
    version=VERSION,
    description="Reference implementation for ndscheduler",
    # url='http://',
    author="Matthias Homann",
    author_email="palto42@mailbox.org",
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
        "Topic :: System",
        "Topic :: Office/Business :: Scheduling",
    ],
    # license = '',
    long_description=readme(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6.4",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "ndscheduler @ git+https://github.com/palto42/ndscheduler.git",
        "requests >= 2.27.1",
        "apns @ git+https://github.com/djacobs/PyAPNs.git"
    ],
    entry_points={"console_scripts": ["simple_scheduler = simple_scheduler:main",]},
    include_package_data=True,
    zip_safe=False,
)
