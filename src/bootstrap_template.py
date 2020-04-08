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

  <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">
  <!-- Custom CSS -->
  <link rel="stylesheet" type="text/css" href="CSS/style.css">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  <!--  Google Font insert font link -->
  <link href="#" rel="stylesheet">
  <!--  Font Awesome 5.x Generate here https://fontawesome.com/start -->

</head>

<body>

  <h1>Hello World!</h1>

  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>

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
