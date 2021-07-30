from core import commands

orig_hidden_file_filter = commands._hidden_file_filter


def _hidden_file_filter(url):
    result = orig_hidden_file_filter(url)
    filename = url.split('/')[-1]
    char1 = filename[0] if filename else None
    char2 = filename[1] if len(filename) >= 2 else None
    if result and char1 == '.' and char2 != '.':
        return False
    return result

commands._hidden_file_filter = _hidden_file_filter
