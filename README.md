## Flask Blueprints Demonstration Project

In this project, we will create a simple Flask web application that demonstrates how Blueprints help organize code into modules. The application will consist of three parts:

- **Main page** (no prefix) – blue window.
- **User part** (prefix `/user`) – gray window.
- **Admin part** (prefix `/admin`) – pink window.

Each module has its own templates, static files (CSS), and routes. This clearly illustrates the isolation of styles and functionality.

---

### 1. Project Structure

```
myapp/
├── app.py                      # Main application file
├── static/                      # Global static files (for main page)
│   └── style.css
├── templates/                   # Global templates
│   └── index.html
├── user/                        # User module
│   ├── __init__.py
│   ├── routes.py                # User module routes
│   ├── static/
│   │   └── style.css            # Styles for user part
│   └── templates/
│       └── user/                 # User module templates
│           ├── index.html        # For /user/
│           └── profile.html      # For /user/profile
└── admin/                       # Admin module
    ├── __init__.py
    ├── routes.py                 # Admin module routes
    ├── static/
    │   └── style.css             # Styles for admin part
    └── templates/
        └── admin/                 # Admin module templates
            ├── index.html         # For /admin/
            ├── profile.html       # For /admin/profile
            └── users.html         # For /admin/users
```

### 2. Running and Testing

1. Make sure all files are placed according to the structure.
2. Install Flask if you haven't already:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to the following URLs:

| URL | Expected Result |
|-----|-----------------|
| `http://127.0.0.1:5000/` | Blue background, text «Hello, human being.» |
| `http://127.0.0.1:5000/user/` | Gray background, text «Hello, human being.» |
| `http://127.0.0.1:5000/user/profile` | Gray background, text «Your profile.» |
| `http://127.0.0.1:5000/admin/` | Pink background, text «Hello, human being.» |
| `http://127.0.0.1:5000/admin/profile` | Pink background, text «Your profile.» |
| `http://127.0.0.1:5000/admin/users` | Pink background, list: John, Carla, Mathew |

---

### 3. What This Project Demonstrates

- **Modularity**: each functional block (user, admin) is separated into its own package with its own routes, templates, and static files.
- **Style Isolation**: thanks to separate `static` folders and the use of `url_for('blueprint.static', ...)`, each module uses its own CSS.
- **Routing Flexibility**: using `url_prefix`, all routes of a module automatically get a common prefix.
- **Name Reuse**: different blueprints can have routes with the same relative paths (e.g., `/profile`) without conflicts.
- **Proper Template Organization**: inside each blueprint’s `templates` folder, a subfolder named after the blueprint is created, preventing accidental file name collisions.

This example serves as an excellent starting point for building larger Flask applications with a clean architecture.