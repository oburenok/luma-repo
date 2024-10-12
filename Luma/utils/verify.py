from utils import globl, log


def is_equal(a, b, msg=None,):
    """
    This function verifies that a and b are equal.

    .. function:: is_equal

    :param a: Actual value
    :type a: var
    :param b: Value to compare with
    :type b: var
    :param msg: Message passed to assert Equal
    :type msg: str

    Examples:
            s = "hello world"
            verify.equal(s.split(), ['hello', 'world'])
    """
    try:
        globl.test_counters['total_checkpoints'] += 1
        log.message(str(msg))

        if a == b:
            log.message(f"Value {a} is equal to value {b}.")
        else:
            log.warning(f"Value {a} is NOT equal to the value {b}.")

    except Exception as exc:
        log.exception(str(exc))

