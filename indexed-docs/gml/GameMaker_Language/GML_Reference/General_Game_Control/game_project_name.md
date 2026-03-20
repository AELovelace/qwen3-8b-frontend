# game\_project\_name

This **read only** variable returns the name of your GameMaker project.

 

#### Syntax:

game\_project\_name

 

#### Returns:

[String](../../GML_Overview/Data_Types.md)

 

#### Example:

var file \= game\_project\_name \+ ".ini";  

 ini\_open(file);  

 ini\_write\_real("Scores", "Highscore", score);  

 ini\_close();

The above code gets the project name and uses it to open (or create) an ini file which is then written to.
