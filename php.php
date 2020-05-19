
<?php
echo '<pre>';

// Mostra todo o resultado do comando do shell "ls", e retorna
// a última linha da saída em $last_line. Guarda o valor de retorno
// do comando shell em $retval.
$last_line = system('ls', $retval);

// Mostrando informação adicional
echo '
</pre>
<hr />Última linha da saída: '.$last_line.'
<hr />Valor de Retorno: '.$retval;
?>
