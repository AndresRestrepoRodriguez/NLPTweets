$(document).ready(function() {

  var popCanvas = $("#popChart");
  var popCanvasDos = $("#popChartDos");
  var popCanvasTres = $("#popChartTres");
  var popCanvasCuatro = $("#popChartCuatro");
  var popCanvasCinco = $("#popChartCinco");
  var popCanvasSeis = $("#popChartSeis");
  var contadorAnalizar=0;
  var graficoUno;
  var graficoDos;
  var graficoTres;
  var graficoCuatro;
  var graficoCinco;
  var graficoSeis;

    $( "#addWord" ).click(function() {
    if (!$('#words').val()){
      swal({
            title: "Oops!",
            text: "No dejes el espacio en blanco",
            icon: "warning"
          });
    }
    else{
      pal=$('#words').val();
      $('#wordAdd').append($('<option>', {
          value: pal,
          text : pal
      }));
      $('#words').val('');
    }
  });

  $( "#removeWord" ).click(function() {
      wordToRemove=$('#wordAdd').val();
      $("#wordAdd option[value='"+wordToRemove+"']").remove();
    })

  $( "#addPhrase" ).click(function() {
    if (!$('#phrase').val()){
      swal({
            title: "Oops!",
            text: "No dejes el espacio en blanco",
            icon: "warning"
          });
    }
    else{
      pal=$('#phrase').val();
      pal="\""+pal+"\""
      $('#phraseAdd').append($('<option>', {
          value: pal,
          text : pal
      }));
      $('#phrase').val('');
    }
  });

  $( "#removePhrase" ).click(function() {
      phraseToRemove=$('#phraseAdd').val();
      $("#phraseAdd option[value='"+phraseToRemove+"']").remove();
    })

  $( "#addHashtag" ).click(function() {
    if (!$('#hashtag').val()){
      swal({
            title: "Oops!",
            text: "No dejes el espacio en blanco",
            icon: "warning"
          });
    }
    else{
      pal=$('#hashtag').val();
      pal="#"+pal;
      $('#hashtagAdd').append($('<option>', {
          value: pal,
          text : pal
      }));
      $('#hashtag').val('');
    }
  });

  $( "#removeHashtag" ).click(function() {
      hashtagToRemove=$('#hashtagAdd').val();
      $("#hashtagAdd option[value='"+hashtagToRemove+"']").remove();
    })

  $( "#addAccount" ).click(function() {
    if (!$('#account').val()){
      swal({
            title: "Oops!",
            text: "No dejes el espacio en blanco",
            icon: "warning"
          });
    }
    else{
      pal=$('#account').val();
      pal="@"+pal;
      $('#accountAdd').append($('<option>', {
          value: pal,
          text : pal
      }));
      $('#account').val('');
    }
  });

  $( "#removeAccount" ).click(function() {
      accountToRemove=$('#accountAdd').val();
      $("#accountAdd option[value='"+accountToRemove+"']").remove();
    })

  $( "#makeAnalysis" ).click(function() {
      if( !$('#wordAdd').has('option').length > 0 && !$('#phraseAdd').has('option').length > 0 && !$('#hashtagAdd').has('option').length > 0 && !$('#accountAdd').has('option').length > 0 ){
        swal({
              title: "Oops!",
              text: "No ingresaste términos para la búsqueda",
              icon: "error"
            });
      }
      else{
        contadorAnalizar++;
        /*
        if (contadorAnalizar > 1){

          graficoUno.destroy();
          graficoDos.destroy();
          graficoTres.destroy();
          graficoCuatro.destroy();
          graficoCinco.destroy();
          graficoSeis.destroy();

        }*/

        var words = $("#wordAdd>option").map(function() { return $(this).val(); });
        var phrases = $("#phraseAdd>option").map(function() { return $(this).val(); });
        var hashtags = $("#hashtagAdd>option").map(function() { return $(this).val(); });
        var accounts = $("#accountAdd>option").map(function() { return $(this).val(); });
        var logicaloption = $("input[name='logicalOperator']:checked").val();
        var json_text = '{}';
        const obj_data = JSON.parse(json_text);
        obj_data["words"] = words;
        obj_data["phrases"] = phrases;
        obj_data["account"] = accounts;
        obj_data["hashtags"] = hashtags;
        obj_data["logicaloption"] = logicaloption;



      }
    })


});