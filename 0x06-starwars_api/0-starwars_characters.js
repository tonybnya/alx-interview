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
  const options = {
    uri: url,
    json: true,
  };

  return request(options);
};

const main = async () => {
  try {
    const response = await requester(charsURL);

    for await (const url of response.characters.map(requester)) {
      log(url.name);
    }
  } catch (error) {
    log(`Error: ${error.message}`);
  }
};

main();
