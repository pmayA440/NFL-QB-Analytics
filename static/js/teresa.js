var base_url= "/all-data";
    var url = "/all-data";
    d3.json(url).then(function(response){
      console.log(response);

      var xValues = response.Passing_Yards;
      var sharedValues = response.Year;
      var labels = response.Name;

      var slicedX = xValues.slice(0,50);
      var slicedShared = sharedValues.slice(0,50);
      var slicedLabels = labels.slice(0,50);

      // @TODO: Build a Bubble Chart using the sample data
      var trace = {
        x: slicedX,
        y: slicedShared,
        text: slicedLabels,
        mode: "markers", 
        marker: {
          size: 10,
          color: xValues,
        }
      };
      var data = [trace];
  
      var layout = {
        title: 'Test',
        showlegend: false,
   
      }
      Plotly.newPlot('bubble', data, layout);
    });