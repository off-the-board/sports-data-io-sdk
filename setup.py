from setuptools import setup, find_packages

setup(
    name="sports_data_io_sdk",
    version="0.1.0",
    description="A client to assist in connecting with the sportsdata.io API",
    author="Dan Goodman",
    author_email="danielgoodman5425@gmail.com",
    url="https://github.com/off-the-board/sports-data-io-sdk",
    packages=find_packages(exclude=("docs", "sports_data_io_sdk.tests")),
    setup_requires=[
        "nose==1.3.7",
        "responses=0.10.6",
    ],
    install_requires=[
        "requests==2.12.0",
        "urllib3==1.25.3"
    ],
    zip_safe=False,
)
