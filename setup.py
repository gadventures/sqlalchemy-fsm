from setuptools import setup, find_packages

setup(name='sqlalchemy-fsm',
    version='0.0.1',
    url='https://github.com/gadventures/sqlalchemy-fsm',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'SQLAlchemy>=0.9.4',
    ],
    license='MIT License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
