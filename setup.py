import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter-vscode-server",
    version="0.0.6",
    author="Timothy Liu",
    author_email="timothyl@nvidia.com",
    description="A Jupyter extension to launch VS Code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tlkh/jupyter-vscode-server",
    py_modules=['nbvscode'],
    entry_points={
        'jupyter_serverproxy_servers': [
            'nbvscode = nbvscode:setup_nbvscode',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux ",
    ],
    install_requires=['jupyter-server-proxy'],
)
