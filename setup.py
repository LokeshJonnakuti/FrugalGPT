from setuptools import setup, find_packages

setup(
    name='FrugalGPT',
    version='0.0.1',
    author='Lingjiao Chen, Matei Zaharia, and James Zou',
    author_email='lingjiao@stanford.edu',
    description='The FrugalGPT library',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'cohere',
        'smart-open',
        'jsonlines',
        'anthropic==0.2.10',
        'scikit-learn',
        'evaluate',
        'scipy',
        'pandas',
        'sqlitedict',
        'torch',
        'transformers',
        'accelerate',
        "fickling>=0.1.3,~=0.1.0",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
