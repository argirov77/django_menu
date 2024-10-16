# Tree Menu Project

This is a Django project that implements a tree menu structure. The menu is stored in the database, and it supports nested items. The project uses Django's admin panel to manage menus and menu items.

## Features

- Tree-structured menus with nested items.
- Menu management through Django Admin.
- Active menu items are highlighted based on the current URL.
- Supports multiple menus on a single page.
- Efficient database queries with a single query per menu.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tree_menu_project.git
    cd tree_menu_project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows use: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser for the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the project at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage

1. Create menus and menu items through the Django admin interface.
2. Use the custom template tag to display menus on any page:
    ```django
    {% load menu_tags %}
    {% draw_menu 'main_menu' %}
    ```

3. The menus are automatically expanded based on the current URL.

## Contributing

Feel free to contribute to the project by creating pull requests or opening issues.


