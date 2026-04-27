
def add_average_key_diff(d: dict, k1, k2) -> None:
    avg_key = round((k1 + k2) / 2)
    diff = abs(d[k1] - d[k2])
    d[avg_key] = diff