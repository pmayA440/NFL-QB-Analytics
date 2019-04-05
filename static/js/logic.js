function buildMetadata(sample) {
//base url and whatever is passed thru the function will get us our json object
  var base_url= "/metadata/";
  var url = base_url+sample;
  d3.json(url).then(function(response){
//console log the response so we know the app.py works
    console.log(response);
    var metaData = [response];
// select the main div and clear out of any existing divs, this will allow us to enter/update new information
    var panel = d3.select(".panel-body")
    .html("")
//select all divs (there will be none since we cleared them all out) and bind it to the JSON object. Enter spaces to create new divs (enough for as many objects in the metadata). 
//Use.html to enter the data using strong tag and .classed to give it the panel-body bootstrap class  
    panel.selectAll("div")
    .data(metaData)
    .enter()
    .append("div")
    .classed("panel-body", true)
  })

};
//This function will take in the year route hosted by flask and create a bubblechart
function buildChart(year){
  var base_url= "/metadata/";
  var url = base_url + year
  d3.json(url).then(function(response){
    console.log(response);
      
    var xValues = response.Wins;
    var sharedValues = response.Passing_Yards;
    var labels = response.Name;
      
// Build a Bubble Chart using the data filtered by the year data
    var trace = {
      x: xValues,
      y: sharedValues,
      text: labels,
      mode: "markers", 
      marker: {
      size: xValues,
      color: xValues,
      }
    };
    var data = [trace];
        
    var layout = {
      title: `Passing Yards vs. Wins in ${year}`,
      showlegend: false,
      xaxis:{
        title: {
          text: "Wins"
               }      
            },
      yaxis:{
        title: {
          text: "Passing Yards"
              }
          }         
      };
    Plotly.newPlot('bubble', data, layout);
    });
 }; 
// This function will take in the win/year route and build a bar chart
function buildtop10Win(start,end){
  var base_url= "/wins/";
  var url = base_url + start + "/" + end
  d3.json(url).then(function(response){
      console.log(response);
      console.log(url);
            
      var name_data = response.Name;
      var win_data = response.Wins;
      var yard_data = response.Passing_Yards;

      // The route will already sort by the win column, all we have to do is slice to get the top 10 
      var sliced_names = name_data.slice(0,10);
      var sliced_wins = win_data.slice(0,10);
      var sliced_yards = yard_data.slice(0,10);

      var BarData = [
            {
              x:sliced_names,
              y:sliced_wins,
              hoverinfo: sliced_yards,
              type: 'bar'
            }
          
          ]
      var layout = {
            title: `Top 10 Most Wins by Quarterback from ${start} to ${end}`,
            showlegend: false,
            xaxis:{
              title: {
                text: "Quarterback"
                     }      
                  },
            yaxis:{
              title: {
                text: "Wins"
                    }
                }         
            };   
      Plotly.newPlot('wins', BarData, layout);
        
      });
    };


// This function will take in the tdpass route and build a bar chart 

function buildtop10TDpasses(start,end){
  var base_url= "/td_passes/";
  var url = base_url + start + "/" + end
  d3.json(url).then(function(response){
      console.log(response);
      console.log(url);
                
      var name_data = response.Name;
      var td_data = response.TD_Passes;
      var yard_data = response.Passing_Yards;
    
      // The route will already sort by the td passes column, all we have to do is slice to get the top 10 

      var sliced_names = name_data.slice(0,10);
      var sliced_td = td_data.slice(0,10);
      var sliced_yards = yard_data.slice(0,10);
    
      var BarData = [
            {
              x:sliced_names,
              y:sliced_td,
              hoverinfo: sliced_yards,
              type: 'bar'
            }
              
          ]
      var layout = {
            title: `Top 10 Most TD Passes by Quarterback from ${start} to ${end}`,
            showlegend: false,
            xaxis:{
              title: {
                text: "Quarterback"
                      }      
                  },
            yaxis:{
              title: {
                text: "TD Passes"
                    }
                }         
            };   
      Plotly.newPlot('tds', BarData, layout);
            
      });
    };

// This function will make the selection panel

function init() {
// Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

// Use the list of sample names to populate the select options
  d3.json("/years").then((yearOptions) => {
    yearOptions.forEach((year) => {
      selector
        .append("option")
        .text(year)
        .property("value", year);
    });

    // Use the first sample from the list to build the initial plots
    const firstYear = yearOptions[0];
    const secondYear = yearOptions[10];

    buildChart(firstYear);
    buildMetadata(firstYear);
    buildtop10Win(firstYear, secondYear);
    buildtop10TDpasses(firstYear, secondYear);
  });
};


function optionChanged(newYear) {
  // Fetch new data each time a new sample is selected
  // newYear2 will be newYear's index + 10
  var newYear2 = parseInt(newYear) + 10;
  buildChart(newYear);
  buildMetadata(newYear);
  buildtop10Win(newYear, newYear2);
  buildtop10TDpasses(newYear, newYear2);
};

// Initialize the dashboard
init();
