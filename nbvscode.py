def setup_nbvscode():
    return {
        "command": ["code-server", "-p", "{port}",
                    "--no-auth", "--allow-http", "--disable-telemetry",
                    "-e", "/home/jovyan/vscode_extensions/",
                    "-d", "/home/jovyan/vscode/"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }
