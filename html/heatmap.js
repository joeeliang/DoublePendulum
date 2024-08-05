// set the dimensions and margins of the graph
var margin = {
    top: 60,
    right: 75,
    bottom: 60,
    left: 90
},
dim = 1000

width =  document.getElementById("inner").offsetWidth - margin.left - margin.right;
height = document.getElementById("inner").offsetWidth - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
.append("svg")
.attr("width", width + margin.left + margin.right)
.attr("height", height + margin.top + margin.bottom)
.append("g")
.attr("transform",
    "translate(" + margin.left + "," + margin.top + ")");

//Read the data
d3.csv("redoData.csv", function(data) {

// Labels of row and columns -> unique identifier of the column called 'group' and 'variable'
var thetaOne = d3.map(data, function(d) {
    return d.t1;
}).keys()
var thetaTwo = d3.map(data, function(d) {
    return d.t2;
}).keys()

// Build X scales and axis:
var x = d3.scaleBand()
    .range([0, width])
    .domain(thetaTwo)
    .padding(0);
svg.append("g")
    .style("font-size", 15)
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x)
        .tickValues(thetaTwo.filter((d, i) => i % 5 === 0)) // show every 5th tick
        .tickFormat(d3.format(".2f"))
        .tickSize(0))
    .select(".domain").remove()
svg.append("text")
    .attr("x", width / 2)
    .attr("y", height + 40)
    .style("text-anchor", "middle")
    .style("font-size", 18)
    .text("Theta 2"); // Replace with your axis title


// Build Y scales and axis:
var y = d3.scaleBand()
    .range([height, 0])
    .domain(thetaOne)
    .padding(0);
svg.append("g")
    .style("font-size", 15)
    .call(d3.axisLeft(y).tickSize(50)
        .tickValues(thetaOne.filter((d, i) => i % 5 === 0)) // show every 5th tick
        .tickFormat(d3.format(".2f"))
        .tickSize(0))
    .select(".domain").remove()
svg.append("text")
    .attr("x", -height/2)
    .attr("y", - 50)
    .style("font-size", 18)
    .style("text-anchor", "middle")
    .attr("transform", "rotate(-90)")
    .text("Theta 1");

// Build color scale
var myColor = d3.scaleSequential()
    .interpolator(d3.interpolateInferno)
    .domain([0, 2.3])

// create a tooltip
var tooltip = d3.select("#my_dataviz")
    .append("div")
    .style("position", "absolute")
    .style("visibility", "hidden")
    .attr("class", "tooltip")
    .style("background-color", "white")
    .style("border", "solid")
    .style("border-width", "2px")
    .style("border-radius", "5px")
    .style("padding", "5px")

// Three function that change the tooltip when user hover / move / leave a cell
var mouseover = function(d) {
    tooltip
        .style("visibility", "visible");
    d3.select(this)
        .style("stroke", "black")
        .style("opacity", 1)
}
    // .on("click", mouseclick);
var mousemove = function(d) {
    tooltip
        .style("opacity", 1)
        .html("Lyapunov Exponent: " + d.value)
        .style("top", (event.pageY) + "px")
        .style("left", (event.pageX+10) + "px")
}

var click = function(d) {
    openSimulation(d.t1, d.t2)
}

function openSimulation(theta1, theta2) {
    const url = `pendulum.html?theta1=${theta1}&theta2=${theta2}`;
    window.open(url, '_blank', 'width=900,height=900');
}

var mouseleave = function(d) {
    tooltip
        .style("opacity", 0)
    d3.select(this)
        .style("stroke", "none")
        .style("opacity", 1)
}

// add the squares
svg.selectAll()
    .data(data, function(d) {
        return d.t1 + ':' + d.t2;
    })
    .enter()
    .append("rect")
    .attr("x", function(d) {
        return x(d.t2)
    })
    .attr("y", function(d) {
        return y(d.t1)
    })
    .attr("rx", 0)
    .attr("ry", 0)
    .attr("width", x.bandwidth())
    .attr("height", y.bandwidth())
    .style("fill", function(d) {
        return myColor(d.value)
    })
    .style("stroke-width", 4)
    .style("stroke", "none")
    .style("opacity", 1)
    .on("mouseover", mouseover)
    .on("mousemove", mousemove)
    .on("mouseleave", mouseleave)
    .on("click", click)
})
