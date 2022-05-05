# Papershack

Simple document server for papers.

## Install & Run

```bash
git clone https://github.com/davekch/papershack.git && cd papershack
pipenv install
./manage.py migrate
./manage.py createsuperuser
cd webclient/papershack
nvm use lts/gallium   # or nvm install 16.14.0 first
npm install
```

```bash
./manage.py runserver &
cd webclient/papershack
npm run serve
```