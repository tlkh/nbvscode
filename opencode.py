def setup_opencode():
    return {
        "command": ["code-server", "-p", "{port}", "--no-auth", "--allow-http", "-d", "/home/jovyan", "--disable-telemetry", "--user-data-dir", "/home/jovyan/vscode/"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }
