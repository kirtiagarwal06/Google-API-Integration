import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [reviews, setReviews] = useState([]);

  // Fetch reviews from the backend
  useEffect(() => {
    axios.get('http://127.0.0.1:5000/get-reviews') // Adjust the URL if needed based on your backend
      .then(response => {
        setReviews(response.data.reviews);
      })
      .catch(error => {
        console.error('There was an error fetching the reviews!', error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Google My Business Reviews</h1>
      <div>
        {reviews.length > 0 ? (
          reviews.map((review, index) => (
            <div key={index}>
              <h3>{review.author_name}</h3>
              <p>{review.text}</p>
              <hr />
            </div>
          ))
        ) : (
          <p>No reviews available</p>
        )}
      </div>
    </div>
  );
}

export default App;
