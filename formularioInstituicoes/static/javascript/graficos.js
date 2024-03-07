function makeLineChart(context, labels, data, lineColor, fillColor) {
  let chart1 = new Chart(context, {
  type: "line",
  data: {
	 labels: labels,
	 datasets: [
		{
		  label: "Consumo total (L)",
		  pointRadius: 0,
		  pointHitRadius: 50,
		  data: data,
		  borderColor: lineColor,
          tension: .3,
          fill: {
            target: 'origin',
            above: fillColor,   // Area will be red above the origin
            below: fillColor    // And blue below the origin
          },
          responsive: true,
          maintainAspectRatio : false
		}
	 ]
  },
  options: {
	 title: {
		text: "Consumo total mensal",
		display: true
	 },
	 scales: {
        y: {
            suggestedMin: 50,
            suggestedMax: 40000,
            display: false,
        }
     },
     plugins: {
        legend: {
            display: false
        }
    }
  }
});
}

function makePieChart(context, labels, data, colors) {
  let chart2 = new Chart(context, {
  type: "doughnut",
  data: {
	 labels: labels,
	 datasets: [
		{
		  label: "Consumo total no ultimo mês (L)",
		  backgroundColor: colors,
		  data: data
		}
	 ]
  },
  options: {
	 title: {
		text: "Consumo total no ultimo mês",
		display: true
	 }
  }
});
}