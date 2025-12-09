def ensure_odd(x: int) -> int:
    x = int(x)
    return x if x % 2 == 1 else x - 1
