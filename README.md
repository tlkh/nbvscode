# Jupyter VS Code Server

## About jupyter-vscode-server

A Jupyter Notebook extension to launch [cdr/code-server](https://github.com/cdr/code-server) (VS Code).

## Using jupyter-vscode-server

You must already have code-server installed. Check out code-server's [Getting Started](https://github.com/cdr/code-server#getting-started) section.

Extension can be install with:

```bash
pip install jupyter-vscode-server
```

Example Dockerfile segment to install code-server:

```Dockerfile
ENV CODESERVER_URL="https://github.com/cdr/code-server/releases/download/1.1119-vsc1.33.1/code-server1.1119-vsc1.33.1-linux-x64.tar.gz" \
    CODESERVER="code-server1.1119-vsc1.33.1-linux-x64"

RUN wget ${CODESERVER_URL} && \
    tar xvf ${CODESERVER}.tar.gz && \
    mv ${CODESERVER}/code-server /usr/local/bin/ && \
    rm -rf code-server* && \
    rm -rf /tmp/* && \
    rm -rf $HOME/.cache && \
    rm -rf $HOME/.node-gyp && \
    fix-permissions $CONDA_DIR && \
    fix-permissions $HOME
```
