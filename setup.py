from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='universal-answer',
    packages=['universal-answer'],
    version='1.0.2',
    license='MIT',
    description='Useless package created for application packaging purpose',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Steve De Jongh',
    author_email='dejongh.st@gmail.com',
    url='https://github.com/sdejongh/universal_answer',
    download_url='https://github.com/sdejongh/universal_answer/raw/master/dist/universal-answer-1.0.2.tar.gz',
    keywords=['h2g2', 'useless', 'dontuse'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Other Audience',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
