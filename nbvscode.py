import os

def setup_nbvscode():
    os.makedirs("/home/jovyan/vscode_projects", exist_ok=True)
    return {
        "command": ["code-server", "-p", "{port}",
                    "--no-auth", "--allow-http", "--disable-telemetry",
                    "-e", "/home/jovyan/.vscode_extensions/",
                    "-d", "/home/jovyan/.vscode_data/",
                    "/home/jovyan/vscode_projects"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }
