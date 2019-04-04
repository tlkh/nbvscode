import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter-vscode-server",
    version="0.0.4",
    author="Timothy Liu",
    author_email="timothyl@nvidia.com",
    description="A Jupyter extension to launch code-server (VS Code)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tlkh/nbvscode",
    py_modules=['opencode'],
    entry_points={
        'jupyter_serverproxy_servers': [
            'opencode = opencode:setup_opencode',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux ",
    ],
    install_requires=['jupyter-server-proxy'],
)
