from setuptools import setup, find_packages
from package import Package
setup(name='mypackage',
version='0.1',
description='Testing installation of Package',
url='#',
author='Giri Sai Ram Ragam',
author_email='girisairam.ragam@automationanywhere.com',
license='NA',
include_package_data=True,
cmdclass={
        "package": Package
    },
packages=find_packages(),
zip_safe=False)