from flask import *
import pickle
import numpy as np
popular = pickle.load(open('static/popular_book.pkl','rb'))
pt = pickle.load(open('static/pt.pkl','rb'))
books = pickle.load(open('static/books.pkl','rb'))
similar = pickle.load(open('static/similar_score.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular['Book-Title'].values),
                           book_author = list(popular['Book-Author'].values),
                           book_img = list(popular['Image-URL-M'].values),
                           book_vote = list(popular['rating-num'].values),
                           book_rating = list(np.round(popular['avg-rating'].values,0)),
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')
@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form['user_input']
    index = np.where(pt.index==user_input)[0][0]
    similar_score = sorted(list(enumerate(similar[index])),key=lambda x:x[1],reverse = True)[1:6]
    data = []
    for i in similar_score:

        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
        #print(data)
        
    return render_template('recommend.html',data = data)

@app.route('/about')
def about():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)
