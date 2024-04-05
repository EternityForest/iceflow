import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iceflow",
    version="0.1.0",
    author="Daniel Dunn",
    author_email="dannydunn@eternityforest.com",
    description="A GStreamer wrapper with JACK connection management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EternityForest/iceflow",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["JACK-Client"],
)


# To push to pypi
# sudo python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*