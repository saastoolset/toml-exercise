import tomli

with open("tic_tac_toe.toml", mode="rb") as fp:
    config = tomli.load(fp)
    
type(config)
print(config)
print(config['user'])
print(config["user"]["player_o"])
