def test_sed():
    import numpy as np
    from mesmer.seds import sync
    arr = sync(np.linspace(10, 100), 23., - 3.)
    arr += 1.
    return True
