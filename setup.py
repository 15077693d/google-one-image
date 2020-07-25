from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Google-one-image',
    url='https://github.com/15077693d/google-one-image',
    author='Oscar Yiu',
    author_email='oscaryiu.lapsang@gmail.com',
    # Needed to actually package something
    packages=['google_one_image'],
    # Needed for dependencies
    install_requires=['selenium'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Enter keyword or list of keyword and get first result in google image:)',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)