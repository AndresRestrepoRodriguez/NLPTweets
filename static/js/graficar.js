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
            text: 'Palabras más Repetidas'
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
                labelString: 'Frecuencia'
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
            text: 'Palabras más Repetidas'

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
            text: 'Palabras más Repetidas'
        },
        scales: {
          xAxes: [{
              position: 'bottom',
              scaleLabel: {
                display: true,
                labelString: 'Frecuencia'
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
            text: 'Palabras más Repetidas'

        }


    }
  });
  return barChart;
}

