# 0x06. Star Wars API

## Description
This repository contains a script (`0-starwars_characters.js`) written in JavaScript that interacts with the Star Wars API to fetch and display information about characters from a specified Star Wars movie. The script prints the names of characters in the order they appear in the movie.

## Algorithm
- **HTTP Requests in JavaScript:**
  - Making HTTP requests to external services using the request module or alternatives like fetch in Node.js.
  - [A Complete Guide to Making HTTP Requests in Node.js](https://www.twilio.com/blog/2017/08/http-requests-in-node-js.html)
- **Working with APIs:**
  - Understanding RESTful APIs and how to interact with them.
  - Parsing JSON data returned by APIs.
  - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)
- **Asynchronous Programming:**
  - Managing asynchronous operations with callbacks, promises, and async/await syntax.
  - Handling API response data asynchronously.
  - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)
- **Command Line Arguments in Node.js:**
  - Using the `process.argv` array to access command-line arguments passed to a Node.js script.
  - [How to Parse Command Line Arguments in Node.js](https://nodejs.dev/learn/how-to-parse-command-line-arguments-nodejs)
- **Array Manipulation and Iteration:**
  - Iterating over arrays and manipulating data structures to format and display character names.
  - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Additional Resources
- [Mock Technical Interview](https://www.interviewbit.com/mock-interview/)
- [Requirements](https://github.com/alexadeveloper/alx-interview/tree/main/0x06-starwars_api#requirements)
- [Tasks](https://github.com/alexadeveloper/alx-interview/tree/main/0x06-starwars_api#tasks)

## Requirements
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- All files end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the folder of the project
- Code should be semistandard compliant (Rules of Standard + semicolons on top)
- All files must be executable
- No usage of `var`
- [More Info](https://github.com/alexadeveloper/alx-interview/tree/main/0x06-starwars_api#more-info)

## Installation
### Node.js 10
``` sudo apt-get install -y nodejs```

### Semi-Standard
```sudo npm install semistandard --global```
### Request module
```
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Usage
```bash
./0-starwars_characters.js <Movie_ID>
```

- `<Movie_ID>`: The ID of the Star Wars movie. For example, 3 corresponds to "Return of the Jedi".

## example

```
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## Author
- [GitHub repository](https://github.com/i-christian/alx-interview)
- Directory: `0x06-starwars_api`
- File: `0-starwars_characters.js`
