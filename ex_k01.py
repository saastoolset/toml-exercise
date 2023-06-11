import tomlkit

toml_data = """
[nested]  # Not necessary

    [nested.table]
    string       = "Hello, TOML!"
    weird_string = '''Literal
        Multiline'''
"""
print(tomlkit.dumps(tomlkit.loads(toml_data)))

print(tomlkit.dumps(tomlkit.loads(toml_data)) == toml_data)