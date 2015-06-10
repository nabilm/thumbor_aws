# coding: utf-8

from setuptools import setup, find_packages

setup(
	name = 'thumbor_aws',
	version = "1",
	description = 'Thumbor AWS extensions',
	author = 'William King. fixed/enhanced by Mohamed Nabil ',
	author_email = 'willtrking@gmail.com, m.nabil.hafez@gmail.com',
	zip_safe = False,
	include_package_data = True,
	packages=find_packages(),
	requires=['dateutil','thumbor','boto']
)
