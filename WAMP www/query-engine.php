<?php



function query ($return_type, $param_type, $param_value) {
	return "SELECT DISTINCT " . return_attributes($return_type) . " FROM " . tables($return_type, $param_type) . " WHERE " . select($return_type, $param_type, $param_value);
}

?>
