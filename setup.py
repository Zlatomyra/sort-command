from setuptools import setup, find_packages

setup(
    name="Zlatomyra-my-sort",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "my-sort = my_sort.main:main",
        ]
    },
    author="Zlatomyra",
    description="Custom sort command implementation",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zlatomyra/sort-command.git",
    python_requires=">=3.7",
)