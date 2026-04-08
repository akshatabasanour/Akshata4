from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    portfolio_data = {
        "name": "Akshata",
        "education": [
            {
                "level": "SSLC",
                "institution": "Ravindra School",
                "description": "Completed secondary schooling with distinction, laying a strong foundation in core sciences and mathematics."
            },
            {
                "level": "PUC (Pre-University Education)",
                "institution": "SMM College",
                "description": "Specialized in pre-university stream with a focus on advanced technical studies and academic excellence."
            },
            {
                "level": "B.E. (Graduation)",
                "institution": "Guru Nanak Dev Engineering College",
                "description": "Currently pursuing Graduation (Bachelor of Engineering) specializing in Computer Science, focusing on advanced engineering principles and research."
            }
        ],
        "certificates": [
            "IEEE Student Membership",
            "Mini Hackathon - Technical Excellence Award",
            "Database Management Systems (DBMS) - NPTEL Certification",
            "Data Structures and Algorithms (DSA) - Advanced Level"
        ],
        "achievements": [
            "Participated in Hackathon - Actively engaged in collaborative problem-solving and software development workshops."
        ],
        "skills": ["Python", "C Language", "OOPs with Java", "DSA"],
        "hobbies": ["Reading Books", "Drawing", "Listening to Music"],
        "languages": ["Kannada", "English", "Hindi", "Telugu"]
    }
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
