def color_code(open_line, live_line):
    """Return color string based on difference between opening and live line."""
    diff = live_line - open_line
    if diff >= 10:
        return 'blue'
    elif diff >= 7:
        return 'green'
    else:
        return 'red'


def sample_games():
    """Return sample games with lines and color codes."""
    games = [
        {"team": "Team A vs Team B", "open": 100, "live": 112},
        {"team": "Team C vs Team D", "open": 95, "live": 102},
        {"team": "Team E vs Team F", "open": 110, "live": 108},
    ]
    for g in games:
        g["color"] = color_code(g["open"], g["live"])
    return games
