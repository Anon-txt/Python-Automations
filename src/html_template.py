#!/usr/bin/env python

import os
import shutil

path = os.getcwd()
print("Cartella corrente: %s" % path)
check = input("Vuoi continuare in questa cartella? y/n ")
if check in ['y', 'Y', 'yes', 'Yes', 'YES']:
    name = input("Scegli nome progetto: ")
    dirNomeProgetto = path + "/" + name
    dirCSS = dirNomeProgetto + "/CSS"
    dirJS = dirNomeProgetto + "/js"
    dirIMG = dirNomeProgetto + "/img"
    indexPath_tmp = path + "/index.html"
    indexPath = dirNomeProgetto + "/index.html"
    stylePath_tmp = path + "/style.css"
    styleCssPath = dirCSS + "/style.css"
    os.mkdir(dirNomeProgetto)
    os.mkdir(dirCSS)
    os.mkdir(dirJS)
    os.mkdir(dirIMG)
    contentIndex = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Title</title>

  <!-- Custom CSS -->
  <link rel="stylesheet" type="text/css" href="CSS/style.css">

</head>

<body>

  <h1>Hello World!</h1>

  <!-- Optional JavaScript -->

  <!-- jQuery  -->
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
</body>

<footer>

</footer>

</html>
    """
    contentStyle = """
body, html {
  font-family: /* Insert Font */ ;
}

/* -------------------------------------------------------------------------------- */
/* ! Tablet */
/* -------------------------------------------------------------------------------- */

@media (max-width: 998px) {}

/* -------------------------------------------------------------------------------- */
/* ! Smartphone */
/* -------------------------------------------------------------------------------- */

@media (max-width: 767px) {}

/* ! Box Sizing */
*,
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
    """
    f = open("index.html", "w")
    f.write(contentIndex)
    f.close
    shutil.move(indexPath_tmp, indexPath)
    f = open("style.css", "w")
    f.write(contentStyle)
    f.close
    shutil.move(stylePath_tmp, styleCssPath)
else:
    print("Sposta il file htmlTemplate.py nella cartella desiderata")
