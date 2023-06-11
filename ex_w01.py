import to_toml

config = {
    "user": {
        "player_x": {"symbol": "X", "color": "blue", "ai": True},
        "player_o": {"symbol": "O", "color": "green", "ai": False},
        "ai_skill": 0.85,
    },
    "board_size": 3,
    "server": {"url": "https://tictactoe.example.com"},
}
print(to_toml.dumps(config))
