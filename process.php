<?php
$numbers = $_GET['separatednumbers'];
$threshold = $_GET['threshold'];

$command = escapeshellcmd("python3 process.py $number $threshold");

$output = shell_exec($command);
echo $output;
?>