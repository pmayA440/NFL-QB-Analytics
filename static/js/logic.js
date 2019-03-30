

      function buildChart(year){
        var base_url= "/metadata/";
          var url = base_url + year
          d3.json(url).then(function(response){
            console.log(response);
      
            var xValues = response.Wins;
            var sharedValues = response.Passing_Yards;
            var labels = response.Name;
      
            var slicedX = xValues.slice(0,48);
            var slicedShared = sharedValues.slice(0,48);
            var slicedLabels = labels.slice(0,48);
      
            // @TODO: Build a Bubble Chart using the sample data
            var trace = {
              x: slicedX,
              y: slicedShared,
              text: slicedLabels,
              mode: "markers", 
              marker: {
                size: slicedX,
                color: xValues,
              }
            };
            var data = [trace];
        
            var layout = {
              title: 'Passing Yards vs. Wins in 1970',
              showlegend: false,
         
            }
            Plotly.newPlot('bubble', data, layout);
          });
        }; 