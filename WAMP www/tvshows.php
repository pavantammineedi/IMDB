<!DOCTYPE html>
<html>
<style>
    .team{
    margin-top: 16px;
    text-align: center;
    font-size: x-large;
}
</style>
  <head>
  <title>Home Page</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">     
  </head>
  <body>
  <nav class="navbar navbar-default" role="navigation">
  <div class="container-fluid" style="padding">        
        <a class="navbar-brand" href="index.php"><i class="bi bi-house" style = "font-size: x-large;"></i></a>
        </div>     
        <p class="team">Team Hydra</li></p>
        </div>
        </nav> 


    <main class="container">

    <?php
      require "query-engine.php";
      require "display-engine.php";

      $Query = " select original_title from titles where title_type = 'tvSeries' limit 100;";
      $Result_Type="tvdetails";
      display_query($Query, $Result_Type);
    ?> 

    </main>
   
  </body>
</html>
