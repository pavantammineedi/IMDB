<?php
function display_query($Query,$Result_Type) {
	$con = pg_connect("host=localhost port=5432 dbname=IMDB user=postgres password=3695");
	echo "<div class='panel panel-default'><div class='panel-body'>" . $Query . "</div></div>";	
	$result = pg_query($con, $Query);

	if($result)
	{
	echo "Success";
	}
	else{
		echo "Failed";	
	}
	
	

	
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



	
