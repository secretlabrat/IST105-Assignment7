<?php
$numbers = $_GET['separatednumbers'];
$threshold = $_GET['threshold'];

$command = escapeshellcmd("python3 bitwise_operations.py $number $threshold");

$output = shell_exec($command);
echo $output;
?>