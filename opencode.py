def setup_opencode():
    return {
        "command": ["code-server", "-p", "{port}", "--no-auth", "--allow-http", "-d", "/home/jovyan"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }
