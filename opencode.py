def setup_opencode():
    return {
        "command": ["code-server", "-p", "{port}", "--password=password"],
        'absolute_url': False
    }
