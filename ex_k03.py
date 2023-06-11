import tomlkit
with open("tic-tac-toe-config.toml", mode="rt", encoding="utf-8") as fp:
    config = tomlkit.load(fp)


print(config)    
print(type(config))

print(config.add("app_name", "Tic-Tac-Toe"))

# print(config["user"].add("ai_skill", 0.6))

config["user"]["ai_skill"] = 0.6
print(config["user"].as_string())