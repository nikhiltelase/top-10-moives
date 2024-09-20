# Movie Ranking Web App

## Overview

This project is a web application for ranking your top 10 favorite movies. Built using Flask, SQLAlchemy, and Bootstrap, the app allows users to add, edit, and delete movies, and it automatically updates movie rankings based on ratings. The app fetches movie data from the OMDb API, ensuring a seamless and user-friendly experience.

## Video
[![Video Thumbnail](https://img.youtube.com/vi/UfxyV3_TnAQ/hqdefault.jpg)](https://www.youtube.com/watch?v=UfxyV3_TnAQ)

Click the image to watch the video.
## LinkedIn Post
[View the LinkedIn post here](https://www.linkedin.com/posts/nikhiltelase_flask-sqlalchemy-python-activity-7209134036449906689-uOm9?utm_source=share&utm_medium=member_desktop)

## Live Demo 
You can view the live version of the project 
[Live Demo](https://top-10-moives.vercel.app/)

## Features

- **Add Movies**: Search and add movies using the OMDb API.
- **Edit Movies**: Update movie ratings and reviews.
- **Delete Movies**: Remove movies from your list.
- **Automatic Ranking**: Movies are ranked based on user ratings.
- **Responsive Design**: Sleek and responsive UI with Bootstrap.

## Technologies Used

- **Flask**: Micro web framework for Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Bootstrap**: Front-end framework for responsive web design.
- **WTForms**: Form validation and rendering library for Flask.
- **OMDb API**: API for retrieving movie data.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nikhiltelase/top-10-moives.git
   cd movie-ranking-app
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the application**:
   ```bash
   flask run
   ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. To add a movie, click on "Add Movie", search for a title, and select from the results.
3. Once a movie is added, you can edit its rating and review by clicking on the "Update" button.
4. To delete a movie, click the "Delete" button next to the movie.

## File Structure

```
movie-ranking-app/
├── instance/
│   └── moive_data.db
├── static/
│   └── styles.css
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   ├── select.html
|   └── base.html
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

## Configuration

- **API Key**: Replace the placeholder API key with your own OMDb API key in `app.py`.
  ```python
  api_key = "your_omdb_api_key_here"
  ```

## Contributing

Contributions are welcome! Please create a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Bootstrap](https://getbootstrap.com/)
- [WTForms](https://wtforms.readthedocs.io/)
- [OMDb API](http://www.omdbapi.com/)

---

