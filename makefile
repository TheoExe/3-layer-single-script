
default:
	@cat makefile

view:
	python db_viewer.py
init:
	python initialize_database.py
test:
	pytest -vvx db_viewer.py

test_smoke:
	pytest -vvx test_create_db.py::test_smoke
clean:
	rm aquarium.db

clean_view: clean init view
