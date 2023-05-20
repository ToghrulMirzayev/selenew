from setuptools import setup

setup(
    name='pylenius',
    version='0.0.1',
    author='Toghrul Mirzayev',
    author_email='togrul.mirzoev@gmail.com',
    description='Pylenius is a framework over Selenium with custom runner to simplify UI Test Automation',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers, Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'selenium',
    ],
    python_requires='>=3.7',
)
