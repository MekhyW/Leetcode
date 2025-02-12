def one_edit_away(first: str, second: str) -> bool:
    if abs(len(first) - len(second)) > 1:
        return False
    longer, shorter = (first, second) if len(first) > len(second) else (second, first)
    i = j = 0
    found_difference = False
    while i < len(longer) and j < len(shorter):
        if longer[i] != shorter[j]:
            if found_difference:
                return False
            found_difference = True
            if len(longer) != len(shorter):
                i += 1
                continue
        j += 1
        i += 1
    return True
