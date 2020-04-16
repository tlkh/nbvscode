import os

def setup_nbvscode():
    os.makedirs("/home/jovyan/vscode_projects", exist_ok=True)
    return {
        "command": ["code-server", "--port", "{port}",
                    "--auth", "none", "--disable-ssh", "--disable-telemetry",
                    "--extensions-dir", "/home/jovyan/.vscode_extensions/",
                    "--user-data-dir", "/home/jovyan/.vscode_data/",
                    "/home/jovyan/vscode_projects"],
        "absolute_url": False,
        "launcher_entry": {
            "title": "VS Code",
        }
    }
