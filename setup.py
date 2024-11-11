from setuptools import setup
import geocrypt
setup(
    name="geocrypt",
    version=geocrypt.version,
    description="Securely encode and decode hexadecimal with geometric figure.",
    long_description="".join(open("README.md","r").readlines()),
    author="lolo859",
    keywords="geocrypt geo crypt",
    classifiers=["Natural Language :: English","Operating System :: OS Independent","Topic :: Security :: Cryptography"],
    py_modules=["geocrypt"],
    install_requires=["sympy>=1.13.3"],
    url="https://github.com/lolo859/geocrypt"
)