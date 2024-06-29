# Book_recommender-

![book1](https://github.com/geetanshudev/Book_recommender-/assets/119582068/cbee851b-0eaa-46d2-b7ff-d22a533f93c4)

![book2](https://github.com/geetanshudev/Book_recommender-/assets/119582068/ed084c52-4e77-4815-872a-c4b260481bb8)

This project presents a book recommender system built with Flask in Python. Users can explore top-rated books and find recommendations based on their specific interests.

**Features:**

* **Home Page:** Displays a list of the top 50 books ranked by calculated rating count.
* **Recommend Page:** Allows users to search for a book and receive recommendations for 5 similar books based on ratings.

**Prerequisites:**

* Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* pip (package installer for Python) - usually comes bundled with Python
* Required libraries (listed in `requirements.txt`)

**Installation:**

1. Clone this repository or download the files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

**Running the Application:**

1. Start the Flask development server:

   ```bash
   python app.py
   ```

2. Open your web browser and visit `http://127.0.0.1:5000/` (replace `127.0.0.1` with your local IP address if necessary).

**Usage:**

* **Home Page:** Browse the list of top 50 recommended books.
* **Recommend Page:** Enter the name of a book in the search bar and submit. The system will recommend 5 similar books based on ratings.

**Note:**

* The accuracy of recommendations depends on the quality of the underlying book data and the recommendation algorithm.
* This is a basic example, and you may customize it further based on your specific data and recommendation techniques (e.g., collaborative filtering, content-based filtering).

**Additional Information:**

* `requirements.txt`: This file lists the required Python libraries for the project.
* `app.py`: This is the main Flask application file. It defines the routes, handles user interactions, and implements the recommendation logic.




**Contributing**

Feel free to fork the repository and submit pull requests with improvements or bug fixes.
