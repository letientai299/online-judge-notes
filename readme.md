Online Judge Notes
==================

Tips and tricks for more convenient during playing on judge site like
Hackerrank...


Goals
-----

- Make the program read input from stdin when running on the website, and from
your `input.txt` when running locally.

- Make logging statement only work if program is running locally.

Scala
-----

```scala
/**
 * Read all lines from stdin or file, depend on where the program is running.
 */
def readLines: List[String] = {
  val lines = if (Files.exists(Paths.get(INPUT_FILE))) {
    Source.fromFile(INPUT_FILE).getLines()
  } else {
    Source.stdin.getLines()
  }
  lines.map(_.trim).toList
}
```

JavaScript
----------

Check if script is running locally

```javascript
var fs = require('fs')

var isOnLocalMachine = function() {
  try {
    return fs.statSync('./app.js').isFile();
  } catch(e) {
    return false;
  }
}

var input = fs.readFileSync('./input.txt').toString('utf8').trim()

// After this line, for debugging purpose, always you log() function
var log = isOnLocalMachine()? console.log.bind(console) : ()=>{}
```

