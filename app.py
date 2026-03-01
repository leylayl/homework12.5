from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET'])
def add_book():
    if request.method == 'POST':
        new_title = request.form.get('title')
        new_autor = request.form.get('author') 
        
        new_id = len(books) + 1
        books.append({"id": new_id, "title": new_title, "author": new_autor})
        return redirect(url_for('index'))
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
    