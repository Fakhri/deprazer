
/*  This visualization was made possible by modifying code provided by:
	
Scott Murray, Choropleth example from "Interactive Data Visualization for the Web" 
https://github.com/alignedleft/d3-book/blob/master/chapter_12/05_choropleth.html   
    	
Malcolm Maclean, tooltips example tutorial
http://www.d3noob.org/2013/01/adding-tooltips-to-d3js-graph.html
	
Mike Bostock, Pie Chart Legend
http://bl.ocks.org/mbostock/3888852  */


//Width and height of map
var width = 960;
var height = 500;

// Define linear scale for output
var color = d3.scale.linear()
    .range(["rgb(206, 206, 206)", "rgb(210, 234, 192)", "rgb(241, 241, 112)", "rgb(234, 93, 93)"]);

var legendText = ["High", "Medium", "Low", "Unavailable"];

//Create SVG element and append map to the SVG
var svg = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

// Append Div for tooltip to SVG
var div = d3.select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

function draw(data, cityData) {
    if (cityData == "California") {
        drawCal(data);
    } else {
        drawUS(data);
    }
}

function drawUS(data) {
    // D3 Projection
    var projection = d3.geo.albersUsa()
        .translate([width / 2, height / 2])    // translate to center of screen
        .scale([1000]);

    // Define path generator
    var path = d3.geo.path()               // path generator that will convert GeoJSON to SVG paths
        .projection(projection);  // tell path generator to use albersUsa projection

    color.domain([0, 1, 2, 3]); // setting the range of the input data

    // Load GeoJSON data and merge with states data
    d3.json("/static/data/us-states.json", function (json) {

        // Loop through each state data value in the .csv file
        for (var i = 0; i < data.length; i++) {

            // Grab State Name
            var dataState = data[i].state;

            // Grab data value 
            var dataValue = data[i].depression;

            var dataKeywords = data[i].keywords;

            // Find the corresponding state inside the GeoJSON
            for (var j = 0; j < json.features.length; j++) {
                var jsonState = json.features[j].properties.name;

                if (dataState == jsonState) {

                    // Copy the data value into the JSON
                    json.features[j].properties.depression = dataValue;
                    json.features[j].properties.keywords = dataKeywords;

                    // Stop looking through the JSON
                    break;
                }
            }
        }

        // Bind the data to the SVG and create one path per GeoJSON feature
        svg.selectAll("path")
            .data(json.features)
            .enter()
            .append("path")
            .attr("d", path)
            .style("stroke", "#fff")
            .style("stroke-width", "1")
            .style("fill", function (d) {

                // Get data value
                var value = d.properties.depression;

                if (value > 0.7) {
                    return color(3);
                } else if (value > 0.5) {
                    return color(2);
                } else if (value > 0.2) {
                    return color(1);
                } else {
                    return color(0);
                }
            })
            // Modification of custom tooltip code provided by Malcolm Maclean, "D3 Tips and Tricks" 
            // http://www.d3noob.org/2013/01/adding-tooltips-to-d3js-graph.html
            .on("mouseover", function (d) {
                div.transition()
                    .duration(200)
                    .style("opacity", .9);
                div.text(d.properties.keywords)
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
            })

            // fade out tooltip on mouse out               
            .on("mouseout", function (d) {
                div.transition()
                    .duration(500)
                    .style("opacity", 0);
            })

            .on("click", function (d) {
                console.log(d.properties.name);
                if (d.properties.name == "California") {
                    window.open(window.location + d.properties.name);
                }
            });
        
        // Modified Legend Code from Mike Bostock: http://bl.ocks.org/mbostock/3888852
        var legend = d3.select("body").append("svg")
            .attr("class", "legend")
            .attr("width", 140)
            .attr("height", 200)
            .selectAll("g")
            .data(color.domain().slice().reverse())
            .enter()
            .append("g")
            .attr("transform", function (d, i) { return "translate(0," + i * 20 + ")"; });

        legend.append("rect")
            .attr("width", 18)
            .attr("height", 18)
            .style("fill", color);

        legend.append("text")
            .data(legendText)
            .attr("x", 24)
            .attr("y", 9)
            .attr("dy", ".35em")
            .text(function (d) { return d; });
    });
}

function drawCal(data) {
    var projection = d3.geo.albersUsa()
        .translate([width, height / 2])    // translate to center of screen
        .scale([2000]);
    var path = d3.geo.path()               // path generator that will convert GeoJSON to SVG paths
        .projection(projection);

    color.domain([0, 1, 2, 3]); // setting the range of the input data

    // Load GeoJSON data and merge with states data
    d3.json("/static/data/california.json", function (json) {

        // Loop through each state data value in the .csv file
        for (var i = 0; i < data.length; i++) {

            // Grab State Name
            var dataState = data[i].state;

            // Grab data value 
            var dataValue = data[i].depression;

            var dataKeywords = data[i].keywords;

            // Find the corresponding state inside the GeoJSON
            for (var j = 0; j < json.features.length; j++) {
                var jsonState = json.features[j].properties.name;

                if (dataState == jsonState) {

                    // Copy the data value into the JSON
                    json.features[j].properties.depression = dataValue;
                    json.features[j].properties.keywords = dataKeywords;

                    // Stop looking through the JSON
                    break;
                }
            }
        }

        // Bind the data to the SVG and create one path per GeoJSON feature
        svg.selectAll("path")
            .data(json.features)
            .enter()
            .append("path")
            .attr("d", path)
            .style("stroke", "#fff")
            .style("stroke-width", "1")
            .style("fill", function (d) {

                // Get data value
                var value = d.properties.depression;

                if (value > 0.7) {
                    return color(3);
                } else if (value > 0.5) {
                    return color(2);
                } else if (value > 0.2) {
                    return color(1);
                } else {
                    return color(0);
                }
            })
            // Modification of custom tooltip code provided by Malcolm Maclean, "D3 Tips and Tricks" 
            // http://www.d3noob.org/2013/01/adding-tooltips-to-d3js-graph.html
            .on("mouseover", function (d) {
                div.transition()
                    .duration(200)
                    .style("opacity", .9);
                div.text(d.properties.keywords)
                    .style("left", (d3.event.pageX) + "px")
                    .style("top", (d3.event.pageY - 28) + "px");
            })

            // fade out tooltip on mouse out               
            .on("mouseout", function (d) {
                div.transition()
                    .duration(500)
                    .style("opacity", 0);
            })

            .on("click", function (d) {
                console.log(d.properties.name);
            });

        // Modified Legend Code from Mike Bostock: http://bl.ocks.org/mbostock/3888852
        var legend = d3.select("body").append("svg")
            .attr("class", "legend")
            .attr("width", 140)
            .attr("height", 200)
            .selectAll("g")
            .data(color.domain().slice().reverse())
            .enter()
            .append("g")
            .attr("transform", function (d, i) { return "translate(0," + i * 20 + ")"; });

        legend.append("rect")
            .attr("width", 18)
            .attr("height", 18)
            .style("fill", color);

        legend.append("text")
            .data(legendText)
            .attr("x", 24)
            .attr("y", 9)
            .attr("dy", ".35em")
            .text(function (d) { return d; });
    });
}