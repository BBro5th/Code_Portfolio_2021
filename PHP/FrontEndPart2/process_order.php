<!DOCTYPE html>
<html lang="en">
	<head >
	   <meta charset="utf-8">
	   <title>IT-Shirts</title>
	</head>
	<body>
		<h2>Your IT-Shirt Order:</h2>
		<?php 
			//echo the values selected by the user
			echo 'Name: '.$_GET["name"].'<br>';
			echo 'Address: '.$_GET["address"].'<br>';
			echo 'Size: '.$_GET["size"].'<br>';
			echo 'Quantity: '.$_GET["qty"].'<br>';
			echo 'Rush: ';
			if(isset($_GET["rush"])){
				echo "Yes";
			}
		?>      
	</body>
</html>