````markdown
# SliderDjango

A simple Django app to manage and render image sliders (carousels).

---

## 1. Installation

```bash
pip install django-sliders
````

---

## 2. Setup

Add the `slider` app to your Django settings:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'slider',  # Add this line
]
```

---

## 3. Migrate and Manage Sliders

Run migrations to create the necessary database tables:

```bash
python manage.py migrate
```

You can now manage your carousel images through the `Slider` model in the Django admin.

---

## 4. Usage in Templates

Use the `render_slider` template tag to render the carousel in your templates:

```django
{% load slider_tags %}

{% render_slider %}
```

---

✨ Example

In your template file (e.g. `index.html`):

```django
{% load slider_tag %}

<!DOCTYPE html>
<html>
<head>
    <title>My Slider</title>
</head>
<body>
    {% render_slider %}
</body>
</html>
```

```

Nếu bạn cần mình tạo thêm ví dụ Bootstrap carousel hoặc tích hợp slider nâng cao hơn, mình có thể hỗ trợ.
```
