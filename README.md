![](example.png)

# Bento
Minimalist Link-in-Bio Template

A clean, lightweight, single-page website to collect all your essential links in one stylish place.


## Setup

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
DJANGO_SECRET_KEY=your-secret-key
```

Then:

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/


## Customization

Go to http://127.0.0.1:8000/admin/

- **Page** — name, description, photo
- **Buttons** — title and url for each link


## License

GNU GPL v3. See [LICENSE](LICENSE).
