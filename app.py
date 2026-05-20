from flask import Flask, render_template, request, redirect
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")


@app.route("/")
def home():
    return render_template("worker_form.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    photo = request.form["photo"]
    aadhaar = request.form["aadhaar"]
    mobile = request.form["mobile"]
    city = request.form["city"]
    category = request.form["category"]
    experience = request.form["experience"]
    skills = request.form["skills"]
    address = request.form["address"]
    description = request.form["description"]
    rating = request.form["rating"]

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO workers
        (name, photo, aadhaar, mobile, city, category,
        experience, skills, address, description, rating)

        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        name,
        photo,
        aadhaar,
        mobile,
        city,
        category,
        experience,
        skills,
        address,
        description,
        rating
    ))

    conn.commit()

    cur.close()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)