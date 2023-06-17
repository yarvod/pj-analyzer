from setuptools import setup


setup(
    name="pj_analyzer",
    version="0.1",
    description="Phystech.Job vacancy analyzer",
    packages=["pj_analyzer"],
    author_email="yar.vod.ole@gmail.com",
    zip_safe=False,
    url="https://github.com/yarvod/pj-analyzer",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "scikit-learn==1.1.3",
        "nltk==3.7",
    ],
)
