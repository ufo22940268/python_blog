def to_utf8(s):
    if s:
        return s.encode("utf-8", "ignore");
    else:
        return None;
