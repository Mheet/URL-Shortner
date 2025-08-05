# Project ShortStack - A URL Shortener with a Dynamic UI

A fully functional URL shortener built with Python and Flask, featuring a mesmerizing, interactive frontend created with vanilla JavaScript and CSS.

![Project Screenshot](https://i.imgur.com/r6t4zXW.gif) ---

## ✨ Features

* **Core URL Shortening:** Convert long URLs into short, easy-to-share links.
* **Custom Aliases:** Users can provide their own custom names for short links.
* **Random Code Generation:** Automatically generates a unique 6-character code if no alias is given.
* **Persistent Storage:** Uses SQLite to save all links.
* **Error Handling:** Gracefully handles when a user tries to create a duplicate alias.
* **Mesmerizing UI:**
    * Animated gradient background.
    * "Living Constellation" effect with drifting, connecting particles.
    * Custom "liquid" cursor that leaves a speed-sensitive "supernova" particle trail.
    * Ripple/shockwave effect on mouse clicks.

---

## 🚀 Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** HTML5, CSS3 (with custom properties and animations), Vanilla JavaScript (using HTML Canvas)

---

## 🔧 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd shortstack
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