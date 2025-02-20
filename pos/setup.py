from setuptools import find_packages, setup

package_name = 'pos'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'mysql-connector-python', 'pyyaml', 'openai'],
    zip_safe=True,
    maintainer='olin',
    maintainer_email='olin.goog@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service = pos.service:main',
            'card_reader = pos.card_reader:main',
            'scanner = pos.scanner:main',
            'interaction = pos.interaction:main',
            'llmi = pos.llmi:main',
        ],
    },
)
