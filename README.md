# FilmyQuote API

This project contains API base for [**FilmyQuote Chrome Extension**](https://chrome.google.com/webstore/detail/filmyquote/blilgiggcmodgommbfmiihcblfmfgkij?hl=en&)`           

### Features

* Django backend in `./backend`
* Backed by Django Rest Framework
* Makefile to make your life easy

### Development environment setup

These steps will install all required dependencies including development ones, run migrations and start dev server.

```bash
make dev
make migrate
make run
```

### Deployment

These steps will install production dependencies and build our application to `static/dist` folder.

```bash
make prod
make build
```

### Authors

* Shiv Prasad - **Backend** - [shiv-prasad](https://github.com/shiv-prasad)
* Soumya Ranjan Bishi - **Frontend** - [soumyabishi](https://github.com/soumyabishi/)

