from setuptools import setup, find_packages

setup(name='simple-socket-client',
      version='1.2',
      url='https://github.com/webtoucher/simple-socket-client',
      license='BSD-3-Clause',
      author='Alexey Kuznetsov',
      author_email='mirakuru@webtoucher.ru',
      description='Simple TCP socket client',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Operating System :: MacOS',
      ],
      packages=find_packages(),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=[
          'gevent-eventemitter~=2.1',
      ],
      zip_safe=False)
