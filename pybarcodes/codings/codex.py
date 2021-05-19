REFERENCE_NUMBERS = {
    0: "0", 1: "1", 2: "2",
    3: "3", 4: "4", 5: "5",
    6: "6", 7: "7", 8: "8",
    9: "9", 10: "A", 11: "B",
    12: "C", 13: "D", 14: "E",
    15: "F", 16: "G", 17: "H",
    18: "I", 19: "J", 20: "K",
    21: "L", 22: "M", 23: "N",
    24: "O", 25: "P", 26: "Q",
    27: "R", 28: "S", 29: "T",
    30: "U", 31: "V", 32: "W",
    33: "X", 34: "Y", 35: "Z",
    36: "-", 37: ".", 38: " ",
    39: "$", 40: "/", 41: "+",
    42: "%",
}

REFERENCE_DIGITS = {v: k for k, v in REFERENCE_NUMBERS.items()}


CODES = {
    "1": "WNSNNW",
    "2": "NWSNNW",
    "3": "WWSNNN",
    "4": "NNSWNW",
    "5": "WNSWNN",
    "6": "NWSWNN",
    "7": "NNSNWW",
    "8": "WNSNWN",
    "9": "NWSNWN",
    "0": "NNSWWN",
    "A": "WNNSNW",
    "B": "NWNSNW",
    "C": "WWNSNN",
    "D": "NNWSNW",
    "E": "WNWSNN",
    "F": "NWWSNN",
    "G": "NNNSWW",
    "H": "WNNSWN",
    "I": "NWNSWN",
    "J": "NNWSWN",
    "K": "WNNNSW",
    "L": "NWNNSW",
    "M": "WWNNSN",
    "N": "NNWNSW",
    "O": "WNWNSN",
    "P": "NWWNSN",
    "Q": "NNNWSW",
    "R": "WNNWSN",
    "S": "NWNWSN",
    "T": "NNWWSN",
    "U": "WSNNNW",
    "V": "NSWNNW",
    "W": "WSWNNN",
    "X": "NSNWNW",
    "Y": "WSNWNN",
    "Z": "NSWWNN",
    "-": "NSNNWW",
    ".": "WSNNWN",
    " ": "NSWNWN",
    "*": "NSWNWN",
    "$": "NSNSNSNN",
    "/": "NSNSNNSN",
    "+": "NSNNSNSN",
    "%": "NNSNSNSN",
}

GUARD = "NSNWWN"