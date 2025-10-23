import builtins
import pandas as pd


def test_dissolution_display_fallback(monkeypatch):
    """Ensure Dissolution notebook display fallback works when caas_jupyter_tools is missing."""
    # Create dummy results similar to the notebook
    results = pd.DataFrame({
        'Model': ['Logistic', 'First-order'],
        'params': [[1, 0.1, 20], [1, 0.1]],
        'R2': [0.95, 0.90]
    })

    real_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == 'caas_jupyter_tools':
            raise ModuleNotFoundError("No module named 'caas_jupyter_tools'")
        return real_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, '__import__', fake_import)

    try:
        try:
            import caas_jupyter_tools
            used = 'tool'
        except Exception:
            from IPython.display import display, Markdown
            display(Markdown('**Dissolution Fit Results**'))
            display(results)
            used = 'fallback'
    finally:
        monkeypatch.setattr(builtins, '__import__', real_import)

    assert used == 'fallback'
