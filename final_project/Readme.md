**COMPUTATIONAL GRAPHICS - FINAL PROJECT**
=======================================

Daniele Rossi - 438538
--------------------------

**Code organization :**

* [index](index.html) creates some instance variables and calls the function [init](assets/functions/Init.js).
* In Init are created : scene, camera, renderer and other objects used in rendering time, moreover in this function home, door, windows and all other objects created by me are added to the scene.
* The functions [makeWardrobe](assets/functions/makeWardrobe.js), [makeWindow](assets/functions/makeWindow.js), [makeCanvas](assets/functions/makeCanvas.js), [makeLavandino](assets/functions/makeLavandino.js), [makeDoor](assets/functions/makeDoor.js), [makeTv](assets/functions/makeTv.js), [makeLamp](assets/functions/makeLamp.js), [makeDisco](assets/functions/makeDisco.js), [makeWall](assets/functions/makeWall.js), [makePavimento](assets/functions/makePavimento.js) contain the methods to create the interior of the house and all are created by me. Instead [objImporter](assets/functions/objImporter.js) contains the function to import all the obj file used.
* [fpsAnimation](assets/functions/fpsAnimation.js) contains method to manage first person mode.
* At last [utilities](assets/functions/utilities.js) contains some helper method as createMesh or initStats.

