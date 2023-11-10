#!/usr/bin/node
/**
 * Star Wars Characters
 * Using Star Wars API
 * 0-starwars_characters.js
 */

const log = (arg) => console.log(arg);

const process = require('process');
const request = require('request');

const base = 'https://swapi-api.alx-tools.com/api/';
const endpoint = 'films/';
const url = `${base}${endpoint}`;

if (process.argv.length !== 3) {
  process.exit(0);
}

const filmID = process.argv[2];
const charsURL = `${url}${filmID}`;

const requester = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode == 200) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
};

async function main(filmID) {
  const response = await requester(charsURL);

  for (const url of response.characters) {
    const result = await requester(url);
    log(result.name);
  }
}

main(filmID);
