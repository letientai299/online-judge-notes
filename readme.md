Online Judge Notes
==================

Tips and tricks for more convenient when playing on judge sites like
Hackerrank...


Goals
-----

- Make the program read input from stdin when running on the website, and from
your `input.txt` when running locally.

- Make logging statement only work if program is running locally.

> **Disclaimer**
>
> _I'm just a newbie in those Scala, JavaScript and Python languages.
> Solving problems on judge sites is my way to learn them. Hence, the
> tips and trick you find here may not the best way to do the task. Pull
> request or suggestion are always welcomed._


Scala
-----

```scala
import java.nio.file.{Files, Paths}

import scala.io.Source

object Solution {

  val INPUT_FILE = "input.txt"

  def readLines: List[String] = {
    val lines = if (Files.exists(Paths.get(INPUT_FILE))) {
      Source.fromFile(INPUT_FILE).getLines()
    } else {
      Source.stdin.getLines()
    }
    lines.map(_.trim).toList
  }

  def main(args: Array[String]): Unit = {
    println(readLines)
  }
}
```

JavaScript
----------

Check if script is running locally

```javascript
const INPUT_FILE = "./input.txt"
var fs = require('fs')

// Only print debugging statement if this is running on local machine
function isOnLocalMachine() {
  try {
    return fs.statSync(INPUT_FILE).isFile();
  } catch (e) {
    return false;
  }
}

var log = isOnLocalMachine() ? console.log.bind(console) : () => {}

if (isOnLocalMachine()) {
  var input = fs.readFileSync('./input.txt').toString('utf8').trim()
  solve(input);
} else {
  process.stdin.resume();
  process.stdin.setEncoding("ascii");
  input = "";
  process.stdin.on("data", function(d) {
    input += d;
  });

  process.stdin.on("end", function() {
    solve(input)
  });
}

function solve(input) {
  // solution code goes here
}
```

Python
------
```python
import os
import sys

INPUT_FILE = "input.txt"
DEBUG = False

#  Redirect stdin to the input file if it is existed
if os.path.isfile(INPUT_FILE):
    sys.stdin= open(INPUT_FILE)
    DEBUG = True
    pass

# Only print log statement if running in local
def log(*args):
    if DEBUG:
        print("[DEBUG]", *args)


# Utils - you may not need it
def reads(): # read string array
    return input().split()

def read_ints(): # read integer array
    return list(map(int, reads()))


# Use Ctrl-D to stop stdin if you run the program without input.txt file
for line in sys.stdin.read().splitlines():
    log(line)
    print(line)

```

Kotlin
------

```kotlin
import java.io.File
import java.util.*

val inputFile = File("input.txt")

val input: Scanner = if (inputFile.exists()) Scanner(inputFile) else Scanner(System.`in`)

fun main(args: Array<String>) {
  // have fun
}
```


Auto restart program when script change
---------------------------------------

With the setup above, I could test my code with local input, to see if my
algorithm works. But I'm tired of switching from vim to terminal and execute
the script manually (python or js). I use [Nodemon](https://github.com/remy/nodemon) to restart program automatically once file change.

This approach works with other scripting language too.

### Install nodemon with [npm](https://www.npmjs.com/)

```sh
npm install -g nodemon

# Reload path
hash -rf
```

### Config nodemon.json

The following configuration will make nodemon watch for changes on `*.txt`
 or `*.py` file in the working directory.

```json
{
  "verbose": false,
  "watch": ["./"],
  "ext": "txt py",
  "execMap": {
    "py": "python3"
  }
}
```

### Let's nodemon watch your file

```sh
# for python
nodemon script.py

# for nodejs
nodemon script.js
```

Now edit the code in your favorite editor and see the result on the terminal running nodemon.

### Bonus: Config nodemon with package.json

```json
{
  "name": "...",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "nodemon app.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "lodash": "^4.15.0"
  }
}
```

I have not found a solution for non-npm yet. Actually, who want to learn js
without nodejs nowadays?
