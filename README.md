# Project ShortStack - A URL Shortener with a Dynamic UI

A fully functional URL shortener built with Python and Flask, featuring a mesmerizing, interactive frontend created with vanilla JavaScript and CSS.

---

## 📸 Screenshots

The application features a dynamic, multi-layered UI with an animated gradient, a "living constellation" particle system, and a "liquid" cursor that leaves a speed-sensitive trail.

**The Main Interface:**
![Main application interface with animated background and custom cursor](assets/screenshot-result.png)

**Result After Shortening:**
![Result box showing the newly created short link for Google](assets/screenshot-main.png)

---

## ✨ Features

- **Core URL Shortening:** Convert long URLs into short, easy-to-share links.
- **Custom Aliases:** Users can provide their own custom names for short links.
- **Random Code Generation:** Automatically generates a unique 6-character code if no alias is given.
- **Persistent Storage:** Uses SQLite to save all links.
- **Error Handling:** Gracefully handles when a user tries to create a duplicate alias.
- **Mesmerizing UI:**
  - Animated gradient background.
  - "Living Constellation" effect with drifting, connecting particles.
  - Custom "liquid" cursor that leaves a speed-sensitive "supernova" particle trail.
  - Ripple/shockwave effect on mouse clicks.

---

## 🚀 Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML5, CSS3 (with custom properties and animations), Vanilla JavaScript (using HTML Canvas)

---

## 🔧 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Mheet/URL-Shortner.git](https://github.com/Mheet/URL-Shortner.git)
    cd URL-Shortner
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # For Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install Flask
    ```

4.  **Initialize the database:**
    ```bash
    # This only needs to be run once
    python -m flask initdb
    ```

5.  **Run the application in debug mode:**
    ```bash
    python -m flask run --debug
    ```

The application will be available at `http://127.0.0.1:5000`.

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -m "Add MyFeature"`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Create a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

**Mheet Singh**
- **GitHub:** [@Mheet](https://github.com/Mheet)
- **LinkedIn:** [@Mheet](https://www.linkedin.com/in/mheet/)
- **Project Repo:** https://www.shorturl.at/(https://github.com/Mheet/URL-Shortner)
