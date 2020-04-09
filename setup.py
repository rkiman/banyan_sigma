from setuptools import setup

setup(name='banyan_sigma_code',
      #version="0.1.0",
      description='CA Bayesian classifier to identify members of the 27 nearest young associations within 150 pc of the Sun.',
      url='https://github.com/jgagneastro/banyan_sigma',
      author='Jonathan Gagne',
      #author_email='',
      license='MIT',
      packages=['banyan_sigma'],
      install_requires=['numpy','astropy','pandas','scipy','astroquery'],
      zip_safe=False)
