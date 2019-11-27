from distutils.core import setup
setup(
  name = 'robot_testrail_python2',
  packages = ['robot_testrail_python2'],
  version = '0.1',
  license='Apache-2.0',
  description = 'Integration Robot Framework with TestRail for python 2.7',
  author = 'Maria Shyrko',
  author_email = 'shirko_2000@yahoo.com',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['ROBOT', 'TESTRAIL'],
  install_requires=[
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Integration Tools',
    'License :: OSI Approved :: Apache-2.0 License',
    'Programming Language :: Python :: 2.7',
  ],
)