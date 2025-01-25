from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

# HTML form template
form_template = '''
<!doctype html>
<html lang="en">
<head>
    <title>Reader Form</title>
</head>
<body>
    <h1>Reader Form</h1>
    <form method="post">
        Name: <input type="text" name="name" value="{{ name }}"><br>
        Email: <input type="email" name="email" value="{{ email }}"><br>
        <input type="submit" value="Submit">
    </form>
    {% if error %}
        <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
'''

# Database connection function
def connect_db():
    return psycopg2.connect(
        dbname="kristians_database",
        user="kristianlorenc",
        password="databasexY123",
        host="localhost",
        port="5432"
    )

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name").strip()
        email = request.form.get("email").strip()

        if not name or "@" not in email:
            return render_template_string(form_template, error="Invalid data!", name=name, email=email)

        try:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO Readers (name, email) VALUES (%s, %s)", (name, email))
            conn.commit()
            cur.close()
            conn.close()
            return "Data successfully saved!"
        except Exception as e:
            print(f"Database error: {e}")
            return "An error occurred while saving the data."

    return render_template_string(form_template, error=None, name="", email="kristian@pythonexam.com")

if __name__ == "__main__":
    app.run(debug=True)

