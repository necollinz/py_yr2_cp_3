def array_diff(a: list, b: list) -> list:
    res = []
    for x in a:
        if x not in b:
            res.append(x)
    return res


def sum_pairs(nums: list, sum: int) -> list:
    seen = set()
    result = None
    best_index = None

    for i in range(len(nums)):
        need = sum - nums[i]

        if need in seen:
            if best_index is None or i < best_index:
                result = [need, nums[i]]
                best_index = i

        seen.add(nums[i])

    return result


def remove_duplicate_ids(obj: dict) -> dict:
    keys = list(obj.keys())
    keys.sort(key=int)

    used = []
    result = {}

    for key in reversed(keys):
        new_list = []
        for ch in obj[key]:
            if ch not in new_list and ch not in used:
                new_list.append(ch)
        result[key] = new_list
        used.extend(new_list)

    return result


def lazy(n):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            count += 1

            if n == 1:
                return func(*args, **kwargs)

            if n == -1:
                return None

            if n > 0:
                if count % n == 1:
                    return func(*args, **kwargs)
                else:
                    return None
            else:
                k = -n
                if count % k == 0:
                    return None
                else:
                    return func(*args, **kwargs)

        return wrapper
    return decorator