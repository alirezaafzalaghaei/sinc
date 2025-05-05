from setuptools import setup

setup(
    name='sinc',
    version='0.1.0',
    packages=["sinc"],
    description="Sinc Kernel Function",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Alireza Afzal Aghaei',
    author_email='alirezaafzalaghaei@gmail.com',
    url='https://github.com/alirezaafzalaghaei/sinc',
    python_needed='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    license='GPL-3.0',
    install_requires=[
        "numpy",
        "scikit-learn",
        "numba"
    ],
)
