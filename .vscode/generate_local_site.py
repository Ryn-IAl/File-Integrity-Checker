import os

structure = {
    "local_site": [
        ("index.html", "<html><head><title>Home</title></head><body><h1>Welcome to LocalSite</h1></body></html>"),
        ("about.html", "<html><head><title>About</title></head><body><p>This is a local test site.</p></body></html>"),
        ("contact.html", "<html><head><title>Contact</title></head><body><p>Email: local@site.com</p></body></html>"),
        ("login.js", "console.log('Login page loaded.');"),
        ("style.css", "body { font-family: Arial; background: #fefefe; }"),
        ("robots.txt", "User-agent: *\nDisallow: /admin"),
        ("admin.php", "<?php echo 'Admin Panel'; ?>"),
        ("favicon.ico", ""),
    ],
    "local_site/logs": [
        ("access.log", '127.0.0.1 - - [28/Jun/2025:09:00:00] "GET /index.html HTTP/1.1" 200 -')
    ],
    "local_site/assets/css": [
        ("theme.css", "h1 { color: darkblue; }")
    ],
    "local_site/assets/js": [
        ("app.js", "console.log('App script loaded.');")
    ],
    "local_site/images": [
        ("logo.png", "")
    ]
}

# Create folders and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for filename, content in files:
        with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
            f.write(content)

print("✅ Local website-like structure created in 'local_site/' folder.")
