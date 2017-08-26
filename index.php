
<!DOCTYPE html>
<html lang="en">
<head>
    <!--
        ===
        This comment should NOT be removed.

        Charisma v2.0.0

        Copyright 2012-2014 Muhammad Usman
        Licensed under the Apache License v2.0
        http://www.apache.org/licenses/LICENSE-2.0

        http://usman.it
        http://twitter.com/halalit_usman
        ===
    -->
    <meta charset="utf-8">
    <title>Tectornix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Charisma, a fully featured, responsive, HTML5, Bootstrap admin template.">
    <meta name="author" content="Muhammad Usman">

    <!-- The styles -->
    <link id="bs-css" href="css/bootstrap-cerulean.min.css" rel="stylesheet">

    <link href="css/charisma-app.css" rel="stylesheet">
    <link href='bower_components/fullcalendar/dist/fullcalendar.css' rel='stylesheet'>
    <link href='bower_components/fullcalendar/dist/fullcalendar.print.css' rel='stylesheet' media='print'>
    <link href='bower_components/chosen/chosen.min.css' rel='stylesheet'>
    <link href='bower_components/colorbox/example3/colorbox.css' rel='stylesheet'>
    <link href='bower_components/responsive-tables/responsive-tables.css' rel='stylesheet'>
    <link href='bower_components/bootstrap-tour/build/css/bootstrap-tour.min.css' rel='stylesheet'>
    <link href='css/jquery.noty.css' rel='stylesheet'>
    <link href='css/noty_theme_default.css' rel='stylesheet'>
    <link href='css/elfinder.min.css' rel='stylesheet'>
    <link href='css/elfinder.theme.css' rel='stylesheet'>
    <link href='css/jquery.iphone.toggle.css' rel='stylesheet'>
    <link href='css/uploadify.css' rel='stylesheet'>
    <link href='css/animate.min.css' rel='stylesheet'>

    <!-- jQuery -->
    <script src="bower_components/jquery/jquery.min.js"></script>

    <!-- The HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- The fav icon -->
    <link rel="shortcut icon" href="img/favicon.ico">

</head>

<body>
    <!-- topbar starts -->
    <div class="navbar navbar-default" role="navigation" style="align-content: center;"    >

        <div class="navbar-inner" >
            <button type="button" class="navbar-toggle pull-left animated flip">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="index.html" style="text-align: center;"> 
                <span  >Proyecto Lidar</span></a>

            <!-- user dropdown starts -->
            <!-- user dropdown ends -->

            <!-- theme selector starts -->

            <!-- theme selector ends -->


        </div>
    </div>
    <!-- topbar ends -->
<div class="ch-container">
    <div class="row">
        
        <!-- left menu starts -->
        <div class="col-sm-2 col-lg-2">
            <div class="sidebar-nav">
                <div class="nav-canvas">
                    <div class="nav-sm nav nav-stacked">

                    </div>

                    <!--label id="for-is-ajax" for="is-ajax"><input id="is-ajax" type="checkbox"></label-->
                </div>
            </div>
        </div>
        <!--/span-->
        <!-- left menu ends -->

        <noscript>
            <div class="alert alert-block col-md-12">
                <h4 class="alert-heading">Warning!</h4>

                <p>You need to have <a href="http://en.wikipedia.org/wiki/JavaScript" target="_blank">JavaScript</a>
                    enabled to use this site.</p>
            </div>
        </noscript>

        <div id="content" class="col-lg-10 col-sm-10">
            <!-- content starts -->
            <div>

</div>
<div class=" row" >
    <form action="configuraciones.php" method="post" 
    >
<div style="display:inline-block;text-align: center;width: 100%;margin: 0 auto;">

        <div class="col-md-3 col-sm-3 col-xs-6">
            <a data-toggle="tooltip" title="6 new members." class="well top-block" href="#">
                <i class="glyphicon glyphicon-user blue "></i>

                <div>Configurar Lidar</div>
                <div ><select name="lidar">
                    <option value="1">500</option>
                    <option value="2">750</option>
                    <option value="3">1000</option>
                </select></div>
                <span class="notification"></span>
            </a>
        </div>
        <div class="col-md-3 col-sm-3 col-xs-6">
            <a data-toggle="tooltip" title="6 new members." class="well top-block" href="#">
                <i class="glyphicon glyphicon-user red "></i>

                <div>Velocidad Motor Lidar</div>
                <div ><div ><select name="motor">
                    <option value="0">0 hz</option>
                    <option value="1">1 hz</option>
                    <option value="2">2 hz</option>
                    <option value="3">3 hz</option>
                    <option value="4">4 hz</option>
                    <option value="5">5 hz</option>
                    <option value="6">6 hz</option>
                    <option value="7">7 hz</option>
                    <option value="8">8 hz</option>
                    <option value="9">9 hz</option>
                    <option value="10">10 hz</option>
                </select></div></div>
                <span class="notification"></span>
            </a>
        </div>
        <div class="col-md-3 col-sm-3 col-xs-6">
            <a data-toggle="tooltip" title="6 new members." class="well top-block" href="#">
                <i class="glyphicon glyphicon-user green"></i>

                <div>Tamaño Maximo Archivo</div>
                <?php
                echo "
                <div ><input type='textarea' name='archivo' placeholder='Tamano maximo:".shell_exec("echo $(($(df|egrep root|awk '{print $4}')/1024))")." MB' >";?>
                 </div>
                <span class="notification"></span>
            </a>
        </div>
</div>
<div style="display:inline-block;text-align: center;width: 80%;margin: 0 auto;">   
                <small><font color="red">
                 <?php session_start();
		#if(is_file('./LASFILES/listo.las')){
		echo $_SESSION["estado"];
		#exec("sudo rm /var/www/html/LASFILES/listo.las");}
		 ?>
                </font>
                 </small><br>
        <a href='' class='btn btn-primary btn-lg'  ><font color="black"><input  type="submit" value='Crear Archivo de Configuracion'/> </font></a>
</div> <br>

    </form>
</div>
<div style="display:inline-block;text-align: center;width: 80%;margin: 0 auto;">   
                <small><font color="red">
                </font>
                 </small><br>
        <a href='./apagar.php' class=	 'btn btn-primary btn-lg'  ><font color="red"><input  type="submit" value='Apagar Sistema'/> </font></a>
</div>


<div class="row">
    <div class="box col-md-4">
        <div class="box-inner">
            <div class="box-header well" data-original-title="">
                <h2><i class="glyphicon glyphicon-user"></i> Estado de Componentes</h2>

                <div class="box-icon">
                    <a href="#" class="btn btn-minimize btn-round btn-default"><i
                            class="glyphicon glyphicon-chevron-up"></i></a>
                    <a href="#" class="btn btn-close btn-round btn-default"><i
                            class="glyphicon glyphicon-remove"></i></a>
                </div>
            </div>
            <div class="box-content">
                <div class="box-content">
                    <ul class="dashboard-list">
                        <li>
                            <a href="#">
                                <img class="dashboard-avatar" alt="Usman"
                                     src="http://www.gravatar.com/avatar/46056f772bde7c536e2086004e300a04.png?s=50"></a>
                            <strong>Componente</strong> <a href="#">LIDAR
                            </a><br>
                            <strong>Since:</strong> 17/05/2014<br>
                            <strong>Status:</strong> <?php $var =system("python conexionLIDAR.py");?>
                        </li>

                        <li>
                            <a href="#">
                                <img class="dashboard-avatar" alt="Abdullah"
                                     src="http://www.gravatar.com/avatar/46056f772bde7c536e2086004e300a04.png?s=50"></a>
                            <strong>Componente</strong> <a href="#">GPS
                            </a><br>
                            <strong>Since:</strong> 25/05/2014<br>
                            <strong>Status:</strong><?php $var =system("python conexionGPS.py");?>
                        </li>
                        <li>
                            <a href="#">
                                <img class="dashboard-avatar" alt="Sana Amrin"
                                     src="http://www.gravatar.com/avatar/hash"></a>
                            <strong>Componente</strong> <a href="#">IMU</a><br>
                            <strong>Since:</strong> 17/05/2014<br>
                            <strong>Status:</strong><?php $var =system("python conexionIMU.py");?>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
            <div class="box-content row">
                <div class="col-lg-7 col-md-12">
                    <h1>Tectronix Lidar<br>
                        <small>Plataforma web de control y administración de Drones.</small>
                    </h1>
                    <p>Esta plataforma posee todo lo que necesita para poder gestionar correctamente los distintos parametros de control para el sistema de Dron, Lidar, GPS e IMU</p>

                    <p><b>Presione el botón celeste para iniciar</b></p>

                    <p class="center-block download-buttons">
                        <?php
                        session_start();
                        if($_SESSION['muestreo']==1){
                        echo "
                        <a href='' class='btn btn-default btn-lg'>Iniciar Adquisición de Datos</a>
                        <a href='./detenerMuestreo.php' class='btn btn-primary btn-lg'>Detener Adquisición de Datos</a>
                        <br>
                        ";
                        $_SESSION['estado']=NULL;
                        }
                        else{
                        $_SESSION['estado']=NULL;
                        echo " <a href='./muestreo.php' class='btn btn-primary btn-lg'>Iniciar Adquisición de Datos</a>
                        <a href='' class='btn btn-default btn-lg'>Detener Adquisición de Datos</a>
                        <br>";
                        if ($_SESSION['las']==1) {
                            $_SESSION['las']=0;
                                echo "<a href='./las.php' class='btn btn-primary btn-lg'> Generar LAS</a>";
                        }
                        }  
                        ?>
                    </p>
                </div>
                <!-- Ads, you can remove these -->
                <div class="col-lg-5 col-md-12 hidden-xs center-text">
                    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
                    <!-- Charisma Demo 4 -->
                    <ins class="adsbygoogle"
                         style="display:inline-block;width:336px;height:280px"
                         data-ad-client="ca-pub-5108790028230107"
                         data-ad-slot="9467443105"></ins>
                    <script>
                        (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>

                <div class="col-lg-5 col-md-12 visible-xs center-text">
                    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
                    <!-- Charisma Demo 5 -->
                    <ins class="adsbygoogle"
                         style="display:inline-block;width:250px;height:250px"
                         data-ad-client="ca-pub-5108790028230107"
                         data-ad-slot="8957582309"></ins>
                    <script>
                        (adsbygoogle = window.adsbygoogle || []).push({});
                    </script>
                </div>
                <!-- Ads end -->

            </div>
    <!--/span-->

    <!--/span-->
</div><!--/row-->


    <!-- content ends -->
    </div><!--/#content.col-md-0-->
</div><!--/fluid-row-->

    <!-- Ad, you can remove it -->
    <div class="row">
        <div class="col-md-9 col-lg-9 col-xs-9 hidden-xs">
            <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
            <!-- Charisma Demo 2 -->
            <ins class="adsbygoogle"
                 style="display:inline-block;width:728px;height:90px"
                 data-ad-client="ca-pub-5108790028230107"
                 data-ad-slot="3193373905"></ins>
            <script>
                (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
        </div>

    </div>
    <!-- Ad ends -->

    <hr>

    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
         aria-hidden="true">

        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h3>Settings</h3>
                </div>
                <div class="modal-body">
                    <p>Here settings can be configured...</p>
                </div>
                <div class="modal-footer">
                    <a href="#" class="btn btn-default" data-dismiss="modal">Close</a>
                    <a href="#" class="btn btn-primary" data-dismiss="modal">Save changes</a>
                </div>
            </div>
        </div>
    </div>

    <footer class="row">
        <p class="col-md-9 col-sm-9 col-xs-12 copyright">&copy; <a href="http://www.facebook.com/olizamasanchez" target="_blank">Oscar Lizama</a> 2017</p><br>
        
        <p class="col-md-3 col-sm-3 col-xs-12 powered-by">Powered by: <a
                href="http://usman.it/free-responsive-admin-template"><img src="img/logo20.png" width="150px"   /></a></p>
    </footer>

</div><!--/.fluid-container-->

<!-- external javascript -->

<script src="bower_components/bootstrap/dist/js/bootstrap.min.js"></script>

<!-- library for cookie management -->
<script src="js/jquery.cookie.js"></script>
<!-- calender plugin -->
<script src='bower_components/moment/min/moment.min.js'></script>
<script src='bower_components/fullcalendar/dist/fullcalendar.min.js'></script>
<!-- data table plugin -->
<script src='js/jquery.dataTables.min.js'></script>

<!-- select or dropdown enhancer -->
<script src="bower_components/chosen/chosen.jquery.min.js"></script>
<!-- plugin for gallery image view -->
<script src="bower_components/colorbox/jquery.colorbox-min.js"></script>
<!-- notification plugin -->
<script src="js/jquery.noty.js"></script>
<!-- library for making tables responsive -->
<script src="bower_components/responsive-tables/responsive-tables.js"></script>
<!-- tour plugin -->
<script src="bower_components/bootstrap-tour/build/js/bootstrap-tour.min.js"></script>
<!-- star rating plugin -->
<script src="js/jquery.raty.min.js"></script>
<!-- for iOS style toggle switch -->
<script src="js/jquery.iphone.toggle.js"></script>
<!-- autogrowing textarea plugin -->
<script src="js/jquery.autogrow-textarea.js"></script>
<!-- multiple file upload plugin -->
<script src="js/jquery.uploadify-3.1.min.js"></script>
<!-- history.js for cross-browser state change on ajax -->
<script src="js/jquery.history.js"></script>
<!-- application script for Charisma demo -->
<script src="js/charisma.js"></script>


</body>
</html>
