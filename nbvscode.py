def setup_nbvscode():
    return {
        "command": ["code-server", "-p", "{port}",
                    "--no-auth", "--allow-http", "--disable-telemetry",
                    "/home/jovyan/vscode_extensions/", "/home/jovyan/"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }
