<?php

$x_str_all = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
$xall = str_split($x_str_all, 1);


foreach ($xall as $x1) {
    foreach ($xall as $x2) {
        foreach ($xall as $x3) {
            foreach ($xall as $x4) {
                $xxx = $x1 . $x2 . $x3 . $x4;

                $ab = md5($xxx);

                if (substr($ab, 0, 10) == "c2979c7124") {
                    echo($ab);
                }


//                echo($x1.$x2.$x3.$x4."\r\n");

            }
        }
    }
}
?>