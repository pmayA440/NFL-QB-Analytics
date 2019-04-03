var nfl = [];
function buildCharts(name, start, end){
 d3.json(`/all-data/${start}/${end}`).then((data) => {
    // Use d3 to select the panel with id of `#all_data`
    var PANEL = d3.select("#all-data");
    console.log(data)
    nfl = data;
    // Use `.html("") to clear any existing metadata
   PANEL.html("");
  // d3.csv("/all-data", function (error, data) {
  //   if (error) return console.warn(error);

  //  console.log(data);
  // })
  
  
  // log a list of names
  // var names = data.map(data => data.name);
  // console.log("names", names);
  
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    // Object.entries(data.slice(1,10)).forEach(([key, value]) => {
    //   PANEL.append("h6").text(`${key}: ${value}`);
    // });
    data.slice(1,10).map(row => {
      PANEL.append("h6").text(`Name : ${row.Name},${row.Wins},${row['TD Passes']}`)
    })
//  Build a Bar Chart with top 10 Quarterbacks with the most # of pass
  var BarData = [
    {
      x:data.slice(0,10).map(row=>row.Name),
      y:data.slice(0,10).map(row=>row['TD Passes']),
      // hovertext:data.Name,
      // hoverinfo: "hovertext",
      type: 'bar'
    }
  
  ]
  
  Plotly.newPlot('barone', BarData);

// Build a Bar Chart with top 10 Quarterbacks with most # of wins
var BarWins = [
  {
    x:data.slice(0,10).map(row=>row.Name),
    y:data.slice(0,10).map(row=>row['Wins']),
    // hovertext:data.Name,
    // hoverinfo: "hovertext",
    type: 'bar'
  }
];

Plotly.newPlot('bartwo', BarWins);
init();
})
}

// //     // Build a Pie Chart
//     // HINT: You will need to use slice() to grab the top 10 sample_values,
//     // top ten quarterbacks, and labels (10 each).
//     var pieData = [
//       {
//         values: row.data.Name.slice(0, 10),
//         labels: row.data.Wins.slice(0, 10),
//         // hovertext: Wins.slice(0, 10),
//         // hoverinfo: "hovertext",
//         type: "pie"
//       }
//     ];

//     var pieLayout = {
//       margin: { t: 0, l: 0 }
//     };

//     Plotly.plot("pie", pieData, pieLayout);
//   });
// }


 function init() {
//   // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");
  var selector2 = d3.select("#selYearStart");
  var selector3 = d3.select("#selYearEnd");
//   // Use the list of sample names to populate the select options

    var min = 1970;
    var max = 2016;
    for(let i = min; i <= max; i++){
      selector2.append("option").text(i).property("value", i);
      selector3.append("option").text(i).property("value", i);
    }
    nfl.forEach((data2) => {
      console.log(data2)
      selector
        .append("option")
        .text(data2.Name)
        .property("value", data2);
    });

// Use the first sample from the list to build the initial plots
  }

// function optionChanged("bill", start, stop) {
//   // Fetch new data each time a new sample is selected
//   buildCharts(newSample);
//  }
function getNewData() {
  const  start = document.getElementById("selYearStart").value;
  const  end = document.getElementById("selYearEnd").value;
  buildCharts("bill", start, end)
}
// Initialize the dashboard
buildCharts(
  'bill',2006,2016
)
