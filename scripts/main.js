const averages = require(["./avgs.json"]);
var ctx = document.getElementById('myChart').getContext('2d');
ctx.canvas.width  = window.innerWidth;
ctx.canvas.height = window.innerHeight;
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'polarArea',

    // The data for our dataset
    data: {
        labels: ["Danceability", "Energy", "Speechiness", "Acousticness", "Liveness", "Valence"],
        datasets: [{
            label: "Averages of Song Features",
            backgroundColor: ['rgb(255,118,117,0.5)', 'rgb(253,203,110,0.5)', 'rgb(255,234,167,0.5)', 'rgb(85,239,196,0.5)', 'rgb(116,185,255,0.5)', 'rgb(162,155,254,0.5)'],
            borderColor: ['#ff7675', '#fdcb6e', '#ffeaa7', '#55efc4', '#74b9ff', '#a29bfe'],
            data: [averages['danceability'], averages['energy'], averages['speechiness'], averages['acousticness'], averages['liveness'], averages['valence']],
        }]
    },

    // Configuration options go here
    options: {
        scale: {
            ticks: {
                min: 0,
                max: 100
            }
        }
    }
});
