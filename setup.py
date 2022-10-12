# setup.py

from distutils.core import setup

setup(name="py-kcs",
      version="1.0",
      author="David Beazley",
      author_email="dave@dabeaz.com",
      url="http://www.dabeaz.com/py-kcs/index.html",
      description="Encode and Decode Kansas City Standard Cassette Audio Data",
      scripts = ['kcs_encode.py','kcs_decode.py'],
      classifiers = ['Programming Language :: Python :: 3',
                     'Topic :: Multimedia :: Sound/Audio :: Conversion'])

