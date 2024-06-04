d3.select("#title").classed("fancy-title", true).text("My Bar Chart");
/*
var scale = d3.scaleLinear()
scale.domain([0,1]).range([0,100])
scale(0.5)
*/
var nobelData = [{key:'United States', value:336},
  {key:'United Kingdom', value:98},
  {key:'Germany',value:79},
  {key:'France',value:60},
  {key:"Sweden",value:29},
  {key:"Switzerland",value:23},
  {key:"Japan",value:21},
  {key:"Russia",value:19},
  {key:"Netherland",value:17},
  {key:"Austria",value:14}
]
/*
var maxWinners = d3.max(nobelData, function(d){return +d.value})

var color = d3.scaleLinear().domain([-1,0,1]).range(["red","green","blue"])
*/
var buildCrudeBarChart=function(){
  var chartHolder = d3.select("#nobel-bar");
  var margin = { top: 20, right: 20, bottom: 30, left: 40 };
  var boundingRect = chartHolder.node().getBoundingClientRect();
  var width = boundingRect.width - margin.left - margin.right;
  var height = boundingRect.height - margin.top - margin.bottom;
  var barWidth=width/nobelData.length

  var xScale = d3.scaleBand().rangeRound([0,width],0.1)
  var yScale = d3.scaleLinear().range([height,0])


  var svg = d3.select("#nobel-bar")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .classed("chart", true)
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  /*nobelData.forEach(function(d,i){
    svg.append('rect').classed('bar',true).attr("height",d.value).attr("width",barWidth).attr("y",height-d.value).attr("x",i*(barWidth))
  })*/
  var update = function(data){
    xScale.domain(d3.range(data.length));
    yScale.domain([0, d3.max(data.map(function(d){return d.value}))])

    var bars = svg.selectAll('.bar').data(data)
    bars.enter().append('rect').classed('bar',true)

    bars.attr('height',function(d, i){return height-yScale(d.value);}).attr('width',xScale.rangeBands())
    .attr('y',function(d){return yScale(d.value);}).attr('x',function(d, i){return xScale;})
    bars.exit().remove()
  }
  update(nobelData)
}
buildCrudeBarChart()

/*
var svg = d3.select('#nobel-bar .chart')
var bars = svg.selectAll('.bar').data(nobelData)
bars = bars.enter()
bars.append('rect').classed('bar',true).attr('width',10).attr('height',function(d){return d.value}).attr('x',function(d,i){return i* 12})
*/