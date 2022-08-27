from setuptools import setup


setup(
    name='ql_extension',
    version='0.0.1',    
    description='A example Python package',
    #url='https://github.com/shuds13/pyexample',
    author='Marek Kolman',
    author_email='marek.kolman@gmail.com',
    license='MIT',
    #packages=['pyexample'],
    install_requires=['QuantLib',
                      'pandas',                     
                      ],
)