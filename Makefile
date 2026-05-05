PYTHON ?= python3

.PHONY: check context flashcards week day site-sync site-dev site-build site-validate site-preview

check:
	$(PYTHON) scripts/validate_structure.py

context:
	$(PYTHON) scripts/export_context_pack.py

flashcards:
	$(PYTHON) scripts/build_flashcards.py

week:
	$(PYTHON) scripts/new_week.py --week $(WEEK) --slug $(SLUG)

day:
	$(PYTHON) scripts/new_day.py --week $(WEEK) --day $(DAY) --slug $(SLUG)

site-sync:
	$(PYTHON) scripts/sync_site_content.py

site-dev:
	cd site && npm run dev

site-build: site-sync
	cd site && npm run build

site-validate:
	$(PYTHON) scripts/validate_site_content.py

site-preview:
	cd site && npm run preview
