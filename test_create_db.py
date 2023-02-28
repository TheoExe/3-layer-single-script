import pytest,os
import db_viewer

@pytest.fixture
def create_db():
	return db_viewer.initialize_database()

@pytest.fixture
def smoke():
	check = 0
	if os.path.exists("aquarium.db"):
		check = 1
	assert check == 1, "The DB you are searching for is smoke (non-existent!)"

@pytest.mark.testcreate
def test_create(create_db):
	create_db

@pytest.mark.testsmoke
def test_smoke(smoke):
	smoke
