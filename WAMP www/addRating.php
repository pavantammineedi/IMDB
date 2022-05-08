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
      <h1>Add Movie Rating</h1>

      <form role="form" action="addRatingResult.php" method="post">

        <div class="form-group">
          <label for="id1">Title Id</label>
          <input name="id1" type="text" class="form-control" id="id1" placeholder="Title Id" required>
        </div>

        <div class="form-group">
          <label for="rating">Average Rating</label>
          <input name="rating" type="text" class="form-control" id="rating" placeholder="Average Rating">
        </div>

        <div class="form-group">
          <label for="votes">Number of Votes</label>
          <input name="votes" type="text" class="form-control" id="votes" placeholder="Number of Votes">
        </div>

        
        <input type="submit" class="btn btn-default">
      </form>
    </main>
   
  </body>
</html>
