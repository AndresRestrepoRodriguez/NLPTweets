function graficarPalabrasRepetidas(canvas,data,labels){
  var barChart = new Chart(canvas, {
    type: 'horizontalBar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Palabras',
        data: data,
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)'
        ]
      }]
    },
    options: {
        title: {
            display: true,
            text: 'Palabras más Relevantes - Índice TF-IDF'
        },
        scales: {
          xAxes: [{
              position: 'bottom',
              ticks: {
                stepSize: 0.1,
                min: 0,
                max: 1
                },
              scaleLabel: {
                display: true,
                labelString: 'Índice TF-IDF'
              }
          }],
          yAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Palabras'
              }
          }]

        }


    }
  });
  return barChart;
}

function graficarPalabrasRepetidasPie(canvas,data,labels){
  var barChart = new Chart(canvas, {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        label: 'Palabras',
        data: data,
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)',
          'rgba(75, 192, 192, 0.6)',
          'rgba(153, 102, 255, 0.6)'
        ]
      }]
    },
    options: {
        title: {
            display: true,
            text: 'Palabras más Relevantes - Índice TF-IDF'

        }


    }
  });
  return barChart;
}

function graficarSentimientosBar(canvas,data,labels){
  var barChart = new Chart(canvas, {
    type: 'horizontalBar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Palabras',
        data: data,
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)'
        ]
      }]
    },
    options: {
        title: {
            display: true,
            text: 'Tweets por tipo de sentimiento'
        },
        scales: {
          xAxes: [{
              position: 'bottom',
              scaleLabel: {
                display: true,
                labelString: 'Cantidad (Tweets)'
              }
          }],
          yAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Sentimiento'
              }
          }]

        }


    }
  });
  return barChart;
}

function graficarSentimientosPie(canvas,data,labels){
  var barChart = new Chart(canvas, {
    type: 'pie',
    data: {
      labels: labels,
      datasets: [{
        label: 'Palabras',
        data: data,
        backgroundColor: [
          'rgba(255, 99, 132, 0.6)',
          'rgba(54, 162, 235, 0.6)',
          'rgba(255, 206, 86, 0.6)'
        ]
      }]
    },
    options: {
        title: {
            display: true,
            text: 'Tweets por tipo de sentimiento'

        }


    }
  });
  return barChart;
}

