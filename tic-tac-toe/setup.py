from setuptools import setup, find_packages

setup(
    name='tic-tac-toe',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'tic-tac-toe=main:main',  # Adjust this if your main function is located elsewhere
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A command-line interface Tic Tac Toe game',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/tic-tac-toe',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)