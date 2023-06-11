from tomlkit import comment, document, nl, table
toml = document()
toml.add(comment("Written by TOML Kit"))
toml.add(nl())
toml.add("board_size", 3)


print(toml.as_string())


# table

player_x = table()
player_x.add("symbol", "X")
player_x.add("color", "blue")
player_x.comment("Start player")
toml.add("player_x", player_x)
player_o = table()
player_o.update({"symbol": "O", "color": "green"})
toml["player_o"] = player_o


print(toml.as_string())