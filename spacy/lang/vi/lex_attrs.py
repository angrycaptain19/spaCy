from ...attrs import LIKE_NUM


_num_words = [
    "không",
    "một",
    "hai",
    "ba",
    "bốn",
    "năm",
    "sáu",
    "bẩy",
    "tám",
    "chín",
    "mười",
    "trăm",
    "tỷ",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    return text.lower() in _num_words


LEX_ATTRS = {LIKE_NUM: like_num}
