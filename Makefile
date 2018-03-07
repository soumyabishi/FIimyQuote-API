# Use development settings for running django dev server.
export DJANGO_SETTINGS_MODULE=backend.settingsdev

# Initializes virtual environment with basic requirements.
prod:
	sudo pip install -r requirements.txt
	sudo npm install --production

# Installs development requirements.
dev:
	sudo pip install -r requirements.txt
	sudo pip install -r requirements-dev.txt
	sudo npm install

# Runs development server.
# This step depends on `make dev`, however dependency is excluded to speed up dev server startup.
run:
	sudo npm run dev & python ./manage.py runserver

# Creates migrations and migrates database.
# This step depends on `make dev`, however dependency is excluded to speed up dev server startup.
migrate:
	sudo python ./manage.py makemigrations
	sudo python ./manage.py migrate

# Builds files for distribution which will be placed in /static/dist
build: prod migrate
	sudo npm run build

# Cleans up folder by removing virtual environment, node modules and generated files.
clean:
	sudo rm -rf node_modules
	sudo rm -rf static/dist

# Run linter
lint:
	sudo @npm run lint --silent
