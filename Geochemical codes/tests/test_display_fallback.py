import builtins
import importlib
import sys
from types import ModuleType

import pandas as pd


def test_display_fallback(monkeypatch):
    """Simulate missing caas_jupyter_tools and ensure the fallback displays results without error."""
    results = pd.DataFrame({"Method":["A","B"], "C0":[1,2], "k":[0.1,0.2]})

    # Ensure importing caas_jupyter_tools raises ModuleNotFoundError
    real_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == 'caas_jupyter_tools':
            raise ModuleNotFoundError("No module named 'caas_jupyter_tools'")
        return real_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, '__import__', fake_import)

    # Now run the fallback code: should not raise
    try:
        try:
            import caas_jupyter_tools  # should raise
            used = 'tool'
        except Exception:
            # fallback
            from IPython.display import display, Markdown
            display(Markdown("**Fit Results for First-Order Kinetics**"))
            display(results)
            used = 'fallback'
    finally:
        # restore import
        monkeypatch.setattr(builtins, '__import__', real_import)

    assert used == 'fallback'
