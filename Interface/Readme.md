Base de données réalisées en SQL et implémentés dans un login python...

for the sql connection : modify in the C# in the file DataConnection.cs the first line.. MySqlConnection connection = new MySqlConnection("Server=127.0.0.1;port=3306;database=dbSQL;username=root;password=root;");

To add a new game : first add the executable it to the folder \veloMax\Ressource\Games If you have game assets put then if the Folder : \veloMax\bin\Debug\net5.0-windows (There is a folder name Assets already created if necessarry) After that you connect yourself on the interface using : username : admin ; password : admin (look at the SQL file)

One game executable (snake.exe in \veloMax\Ressource\Games\snake) is to big to be put in gitub (limited to 25 Mb files)
