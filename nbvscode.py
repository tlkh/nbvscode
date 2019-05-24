def setup_nbvscode():
    return {
        "command": ["code-server", "-p", "{port}",
                    "--no-auth", "--allow-http", "--disable-telemetry",
                    "--extensions-dir", "/home/jovyan/vscode_extensions/"
                    "--user-data-dir", "/home/jovyan/"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }
