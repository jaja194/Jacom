// js code for slider bar

let slideIndex = 0;
showSlide(slideIndex);

function moveSlide(n) {
  showSlide(slideIndex += n);
}

function showSlide(n) {
  const slides = document.getElementsByClassName('slide');
  if (n >= slides.length) {
    slideIndex = 0;
  }
  if (n < 0) {
    slideIndex = slides.length - 1;
  }
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }
  slides[slideIndex].style.display = 'block';
}


// js code for search bar

// JavaScript code for handling search functionality
document.getElementById('searchForm').addEventListener('submit', function(event) {
  event.preventDefault();
  
  // Get the search query from the input field
  const searchQuery = document.getElementById('searchInput').value;

  // Perform search based on the query (you can use AJAX to fetch results from a server)
  // For demonstration, let's just display the search query as the result
  displaySearchResults(searchQuery);
});

function displaySearchResults(query) {
  const searchResultsDiv = document.getElementById('searchResults');

  // Clear previous search results
  searchResultsDiv.innerHTML = '';

  // Display the search query as the result (you can customize this)
  const searchResultText = document.createElement('p');
  searchResultText.textContent = `Search results for: ${query}`;
  searchResultsDiv.appendChild(searchResultText);
}


// js code for geolocation

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(sendLocationToBackend);
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
}

function sendLocationToBackend(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;

  // Send geolocation data to the backend using Fetch API or AJAX
  fetch('/geolocation/', {
    method: 'POST',
    body: new URLSearchParams({
      'latitude': latitude,
      'longitude': longitude
    }),
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message); // Log success message from backend
    // Handle success response from the backend as needed
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle error response from the backend
  });
}