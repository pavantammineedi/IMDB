<?php
function display_query($Query, $Result_Type) {
		$con = pg_connect("host=localhost port=5432 dbname=IMDB user=postgres password=3695");
	$result = pg_query($con, $Query);

	if($result)
	{
	echo "Success";
	} else{
	echo "Failed";
	}

	echo "<table class='table'>";
	
	switch($Result_Type) {
		
			

		case "DirCumAct":
			echo "<tr><th>Id</th> <th>Name</th></tr>";
			while($row = pg_fetch_array($result)) {
				display_row(array("name_id","name"), $row);
			}
			break;

		

		
		case "actordetails":
			echo "<tr><th>Id</th> <th>Name</th> </tr>";

			while($row = pg_fetch_array($result)) {

			        display_row(array("name_id","name"), $row);
			}
			break;


		case "dirdetails":
			echo "<tr><th>Id</th> <th>Name</th> </tr>";
			while($row = pg_fetch_array($result)) {
				display_row(array("name_id","name"), $row);
			}
			break;

		case "movdetails":
			echo "<tr><th>Movie</th> </tr>";
			while($row = pg_fetch_array($result)) {
			        display_row(array("original_title"), $row);
			}
			break;


		case "tvdetails":
			echo "<tr><th>TV Show</th></tr>";
			while($row = pg_fetch_array($result)) {
				display_row(array("original_title"), $row);
			}
			break;
		
		

		
		

		default:
			break;
	}
	echo "</table>";

	pg_close($con);
}

function display_row($fields, $row) {
	echo "<tr>";
	foreach ($fields as $field) {
		echo "<td>" . $row[$field] . "</td>";
  	}
  	echo "</tr>";
}
?>



	
