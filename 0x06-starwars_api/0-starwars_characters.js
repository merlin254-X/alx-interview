#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make an HTTP GET request to fetch movie details
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body as JSON
  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Function to print character names in the correct order
  const printCharacter = (index) => {
    if (index >= characters.length) return; // Base case for recursion

    // Fetch each character's details using their URL
    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      // Print the character's name
      const character = JSON.parse(charBody);
      console.log(character.name);

      // Recursively print the next character
      printCharacter(index + 1);
    });
  };

  // Start printing from the first character
  printCharacter(0);
});
