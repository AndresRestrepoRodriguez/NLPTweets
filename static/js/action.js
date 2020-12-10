$(document).ready(function() {

  var popCanvas = $("#popChart");
  var popCanvasDos = $("#popChartDos");
  var popCanvasTres = $("#popChartTres");
  var popCanvasCuatro = $("#popChartCuatro");
  var contadorAnalizar=0;
  var graficoUno;
  var graficoDos;
  var graficoTres;
  var graficoCuatro;

  $('#analysis').hide();
  $('#contact').css("display", "none");

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
        if (contadorAnalizar > 1){
          graficoUno.destroy();
          graficoDos.destroy();
          graficoTres.destroy();
          graficoCuatro.destroy();
          $('#analysis').hide();

        }

        var lang = []
        lang.push("hola")
        lang.push("mundo")

        var words = [];
        $('#wordAdd option').each(function() {
                words.push($(this).val());
            });
        var phrases = [];
        $('#phraseAdd option').each(function() {
                phrases.push($(this).val());
            });

        var hashtags = [];
        $('#hashtagAdd option').each(function() {
                hashtags.push($(this).val());
        });

        var accounts = [];
        $('#accountAdd option').each(function() {
                accounts.push($(this).val());
        });
        $('#contactForm').fadeToggle();
        var logicaloption = $("input[name='logicalOperator']:checked").val();
        var json_text = '{}';
        const obj_data = JSON.parse(json_text);
        obj_data["words"] = words;
        obj_data["phrases"] = phrases;
        obj_data["account"] = accounts;
        obj_data["hashtags"] = hashtags;
        obj_data["logicaloption"] = logicaloption;
        console.log(obj_data)
        $.ajax({
        type : 'POST',
        dataType: "JSON",
        data : JSON.stringify(obj_data),
        contentType: "application/json; charset=utf-8",
        url : '/analytics'
        })
        .done(function(data) {
        if(data.response == "Error"){
        contadorAnalizar++;
            $('#contactForm').fadeToggle();
          swal({
                 title: "Oops!",
                 text: data.mensaje,
                 icon: "error"
               });
        }
        else{
           contadorAnalizar++;
           console.log(data.sentimentkeys)
           console.log(data.sentimentvalues)
           console.log(data.tfidfwords)
           console.log(data.tfidfvalues)
           $('#analysis').show();
           graficoUno=graficarSentimientosBar(popCanvas,data.sentimentvalues,data.sentimentkeys);
           graficoDos=graficarSentimientosPie(popCanvasDos,data.sentimentvalues,data.sentimentkeys);
           graficoTres=graficarPalabrasRepetidas(popCanvasTres,data.tfidfvalues,data.tfidfwords);
           graficoCuatro=graficarPalabrasRepetidasPie(popCanvasCuatro,data.tfidfvalues,data.tfidfwords);
           $('#contactForm').fadeToggle();
           }
    });
        }
    });

    $( "#downloadCanvasUno" ).click(function() {
      formatoUno=$("#formatoUno").val();
      download_image("popChart",formatoUno);
    });

    $( "#downloadCanvasDos" ).click(function() {
      formatoDos=$("#formatoDos").val();
      download_image("popChartDos",formatoDos);
    });

    $( "#downloadCanvasTres" ).click(function() {
      formatoTres=$("#formatoTres").val();
      download_image("popChartTres",formatoTres);
    });

    $( "#downloadCanvasCuatro" ).click(function() {
      formatoCuatro=$("#formatoCuatro").val();
      download_image("popChartCuatro",formatoCuatro);
    });

    $( "#sendMail" ).click(function() {
        var doc = new jsPDF();
        var specialElementHandlers = {
            '#editor': function (element, renderer) {
                return true;
            }
        };
         doc.fromHTML($('#analysis').html(), 15, 15, {
            'width': 170,
            'elementHandlers': specialElementHandlers
            });
         doc.save('analysis.pdf');
        console.log('before');
        wait(7000);  //7 seconds in milliseconds
        console.log('after');
        email=$('#emailUser').val();
        var json_text = '{}';
        const obj_data = JSON.parse(json_text);
        obj_data["emailuser"] = email;
        $.ajax({
        type : 'POST',
        data : obj_data,
        url : '/sendmail'
        }).done(function(data) {
        if(data.response == "Error"){
          swal({
                 title: "Oops!",
                 text: "no se pudo enviar el email",
                 icon: "error"
               });
        }
        else{
           console.log(data.response)
           }
    });
    });


});

function wait(ms){
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}