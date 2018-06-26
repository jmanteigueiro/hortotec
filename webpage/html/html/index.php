<!DOCTYPE HTML>
<!--
	Story by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
<head>
    <title>Hortotec</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
</head>
<body class="is-preload">

<!-- Wrapper -->
<div id="wrapper" class="divided">

    <!-- One -->
    <section class="banner style1 orient-left content-align-left image-position-right fullscreen onload-image-fade-in onload-content-fade-right">
        <div class="content">
            <h1>Hortotec</h1>
            <p class="major">Uma estufa inteligente</p>
            <ul class="actions stacked">
                <li><a href="#first" class="button big wide smooth-scroll-middle">Dados atuais</a></li>
                <li><a href="#second" class="button big wide smooth-scroll-middle">Configuração</a></li>
            </ul>
        </div>
        <div class="image">
            <img src="images/plant.jpg" alt="" />
        </div>
    </section>

    <?php
    $file = new SPLFileObject('current_values.txt');
    foreach($file as $line) {
        $data = preg_split("/[,]/", $line);
    }
    // humidity,luminosity,temperature,time
    $humidity = $data[0];
    $luminosity = $data[1];
    $temperature = $data[2];
    $last_update = $data[3];
    ?>

    <section class="spotlight style1 orient-right content-align-left image-position-center onscroll-image-fade-in">
        <div class="content">
            <h2>Dados no momento</h2>
            <section id="first">
                <p>Temperatura:
                    <strong>
                        <?php  echo htmlspecialchars($temperature);?>
                        ºC
                    </strong></p>
                <p>Humidade do Solo:
                    <strong>
                        <?php  echo htmlspecialchars($humidity);?>
                        %
                    </strong>
                </p>
                <p>Luminosidade:
                    <strong>
                        <?php  echo htmlspecialchars($luminosity);?>
                        %
                    </strong></p>
                <p>Última atualização: <?php  echo htmlspecialchars($last_update);?>
                </p>
            </section>
        </div>
        <div class="image">
            <img src="images/plant2.jpg" alt="">
        </div>
    </section>

    <!-- Three -->

    <section class="wrapper style1 align-center">
        <form action="processing.php" method="POST">
            <div class="inner">
                <br>
                <input type="submit" name="submit" class="btn btn-info" value="Save Data">
                <div class="items style1 medium onscroll-fade-in">
                    <section id="second">
                        <span class="icon style2 major fa-lightbulb-o"></span>
                        <h3>Luminosidade</h3>
                        <p><label>Ínício [Horas]</label>
                            <input type="text" style="text-align: center" class="form-control" name="lumini"
                                   aria-describedby="emailHelp" placeholder="07:00"></p>
                        <p><label>Fim [Horas]</label>
                            <input type="text" style="text-align: center" class="form-control" name="lumifim"
                                   aria-describedby="emailHelp" placeholder="20:00"></p>
                        <p><label>Automático [0-100]</label>
                            <input type="text" style="text-align: center" class="form-control" name="lumifx"
                                   aria-describedby="emailHelp" placeholder="50"></p>
                    </section>
                    <section>
                        <span class="icon style2 major fa fa-tint"></span>
                        <h3>Rega</h3>
                        <p><label>Ínício [Horas]</label>
                            <input type="text" style="text-align: center" class="form-control" name="regaxhoras"
                                   aria-describedby="emailHelp" placeholder="19:00"></p>
                        <p><label>Fim [Horas]</label>
                            <input type="text" style="text-align: center" class="form-control" name="regaifhumambiente"
                                   aria-describedby="emailHelp" placeholder="20:00"></p>
                        <p><label>Automático [0-100]</label>
                            <input type="text" style="text-align: center" class="form-control" name="regaifhumsolo"
                                   aria-describedby="emailHelp" placeholder="50"></p>
                        <p><label>Segundos [0-15]</label>
                            <input type="text" style="text-align: center" class="form-control" name="regasegundos"
                                   aria-describedby="emailHelp" placeholder="5">
                    </section>
                    <section>
                        <span class="icon style2 major fa fa-thermometer-3"></span>
                        <h3>Ambiente</h3>
                        <p><label>Temperatura [ºC]</label>
                            <input type="text" style="text-align: center" class="form-control" name="aquecimento"
                                   aria-describedby="emailHelp" placeholder="25"></p>
                    </section>
                </div>
            </div>
        </form>
    </section>

</div>

<!-- Scripts -->
<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/jquery.scrollex.min.js"></script>
<script src="assets/js/jquery.scrolly.min.js"></script>
<script src="assets/js/browser.min.js"></script>
<script src="assets/js/breakpoints.min.js"></script>
<script src="assets/js/util.js"></script>
<script src="assets/js/main.js"></script>

</body>
</html>