import typing

T = typing.TypeVar('T')


def get_with_retry(get_from: object, retry_count: int, fallback_value: T) -> T:
    if retry_count < 0:
        print("falling back to fallback value")
        return fallback_value
    else:
        try:
            return get_from.get()
        except Exception as e:
            print(e)
            print("failed, retrying up to {} more times...".format(retry_count))
            return get_with_retry(get_from, retry_count - 1, fallback_value)
