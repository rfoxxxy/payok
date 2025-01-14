import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as file:
    long_description = "\n" + file.read()

VERSION = "1.0.3"
DESCRIPTION = "Asynchronous PayOK API wrapper"

setup(
    name="payok.io",
    version=VERSION,
    author="Nikita Minaev",
    author_email="<nikita@minaev.su>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["httpx", "Brotli", "pydantic"],
    keywords=[
        "python",
        "payok.io",
        "payments",
        "payok-api",
        "async",
        "asyncio",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url="https://github.com/nikitalm8/payok",
    project_urls={
        "Homepage": "https://github.com/nikitalm8/payok",
        "Bug Tracker": "https://github.com/nikitalm8/payok/issues",
        "API Docs": "https://payok.io/cabinet/documentation/doc_api_main",
    },
)
