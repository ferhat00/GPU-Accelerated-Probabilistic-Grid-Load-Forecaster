# Thin shim delegating to `just`. Keeps muscle memory working (`make test`).
.PHONY: install smoke lint format typecheck test test-gpu bench clean

install smoke lint format typecheck test test-gpu bench clean:
	just $@
