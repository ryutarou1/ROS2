from setuptools import setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
     (os.path.join('share', package_name), glob('launch/*.launch.py'))
        ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ryu',
    maintainer_email='rkanno1014@yahoo.co.jp',
    description='a package for practice',
    license='GPL-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         ' talker = mypkg.talker:main',
         'listener = mypkg.listener:main',
        ],
        },
        ),
