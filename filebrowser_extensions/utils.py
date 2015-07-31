def is_extend_value(value):
    """
    Check if string is from extend media
    """
    # TODO: let's just write regex here
    values = value.split(':')
    if len(values) == 2 and len(value) > 2:
        values = values[0].split('.')
        if len(values) == 2:
            return True
    return False