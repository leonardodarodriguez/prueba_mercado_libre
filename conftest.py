import os
import pytest
from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Sólo interesa al final de la fase de ejecución del test
    if rep.when != "call":
        return

    screenshot_dir = os.path.join(item.config.rootpath, "screenshots")
    if not os.path.isdir(screenshot_dir):
        return

    # Adjunta **todas** las PNG de screenshots/ al reporte
    # en el orden alfabético que las guardaste (01_home, 02_mexico…)
    rep.extra = getattr(rep, "extra", [])
    for fname in sorted(os.listdir(screenshot_dir)):
        if not fname.lower().endswith(".png"):
            continue
        path = os.path.join(screenshot_dir, fname)
        rep.extra.append(extras.image(path))
