<?php

// test to see if threading is available

// function to be ran on separate threads
session_start();
$_SESSION['muestreo']=1;
//$cmd="python muestreo.py";
system("python cliente.py 3");
//exec(sprintf("%s > %s 2>&1 & echo $! >> %s", $cmd, $outputfile, $pidfile));
/*
class WorkerThreads extends Thread
{
    private $workerId;
 
    public function __construct($id)
    {
        $this->workerId = $id;
    }
 
    public function run()
    {
        sleep(rand(0, 3));
        echo "Worker {$this->workerId} ran" . PHP_EOL;
    }
}*/
header("Location: /index.php");
  ?>
