from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Contact Page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if not name or not email or not subject or not message:
            return render_template("contact.html", error="All fields are required.")

        # In real-world use: send email or store in database
        return render_template("contact.html", success="Thank you for your message!")

    return render_template("contact.html")

# Resume Download/View
@app.route("/resume")
def resume():
    # Make sure your_resume.pdf is inside the `resume` folder in the root
    return send_from_directory("resume", "your_resume.pdf")

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
