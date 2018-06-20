<!DOCTYPE html>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />

<html>
<head>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/tempusdominus-bootstrap-4/5.0.0-alpha14/js/tempusdominus-bootstrap-4.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tempusdominus-bootstrap-4/5.0.0-alpha14/css/tempusdominus-bootstrap-4.min.css" />
</head>
<body>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>

<h1>HortoTec</h1>

<form action="processing.php" method="POST">
<div class="row">
    <div class="form-group col-md-2">
        <label>Luminosidade</label>
        <input text="email" class="form-control" name="lumini" aria-describedby="emailHelp" placeholder="07:00">
        <small class="form-text text-muted">Início</small>

        <label></label>
        <input type="text" class="form-control" name="lumifim" aria-describedby="emailHelp" placeholder="20:00">
        <small class="form-text text-muted">Fim</small>

        <label></label>
        <input type="text" class="form-control" name="lumifx" aria-describedby="emailHelp" placeholder="50">
        <small class="form-text text-muted">Auto (quando < x) </small>
    </div>

    <div class="form-group col-md-2">
        <label>Rega</label>
        <input type="text" class="form-control" name="regaxhoras" aria-describedby="emailHelp" placeholder="07:00">
        <small class="form-text text-muted">Às x horas</small>

        <label></label>
        <input type="text" class="form-control" name="regaifhumambiente" aria-describedby="emailHelp" placeholder="50">
        <small id="regaifhumambient" class="form-text text-muted">Humidade < x Ambiente</small>

        <label></label>
        <input type="text" class="form-control" name="regaifhumsolo" aria-describedby="emailHelp" placeholder="50">
        <small class="form-text text-muted">Humidade < x Solo</small>

        <label></label>
        <input type="text" class="form-control" name="regasegundos" aria-describedby="emailHelp" placeholder="5">
        <small class="form-text text-muted">Segundos Rega</small>
    </div>

    <div class="form-group col-md-2">
        <label>Temperatura</label>
        <input type="text" class="form-control" name="aquecimento" aria-describedby="emailHelp" placeholder="25">
        <small class="form-text text-muted">Quando T < x</small>
        </br>

    </div>



</div>

</br>


    <input type="submit" name="submit" class="btn btn-info" value="Save Data">
</form>

<div>
    <label>Humidade Atual</label>
    <?php $fh = fopen('moment_value_humidity.txt','r'); $value = fgets($fh); echo htmlspecialchars($value); fclose($fh); ?>
</div>

</body>
</html>
