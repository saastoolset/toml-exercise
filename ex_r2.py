import tomli

toml_str = """
offset_date-time_utc = 2021-01-12 00:23:45Z
potpourri = ["flower", 1749, { symbol = "X", color = "blue" }, 1994-02-14]
"""

config = tomli.loads(toml_str)
print(config)

