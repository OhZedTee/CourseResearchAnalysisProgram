import React from "react";
import RouteBox from "./../../components/RouteBox";
import Panel from "./../../components/Panel";
import {
  exportSearchDataEdges,
  exportSearchDataNodes,
  getAllExportFiles,
  exportSearchDataEdgesFromFile,
  exportSearchDataNodesFromFile,
} from "./../../api-calls/lib.js";
import {
  getAllCourseWeightData,
  getCourseCode,
  getAllCourseDepartments,
  getAllCourseFaculty,
  filterSearchResults,
  setUpCombineSearch,
  getAllCourseAvailability,
  getAllCourseLevel,
} from "../../api-calls/lib";
import * as d3 from "d3";
import "./GraphPage.css";
import "d3-time-format";
import { objToArray } from "./../../api-calls/commonFuncs.js";
import { colourDictionary } from "./../../api-calls/consts.js";

// This page shows the user all the metrics to search for and when the
// user clicks on one of the options will take them to the page (most pages not created yet)

const createGraph = async (fileName) => {
  try {
    let tempLinks = [];
    let tempNodes = [];

    // Determines whether to load from a file or from the most recent search
    if (fileName === "") {
      tempLinks = await exportSearchDataEdges();
      tempNodes = await exportSearchDataNodes();
    } else {
      tempLinks = await exportSearchDataEdgesFromFile(fileName);
      tempNodes = await exportSearchDataNodesFromFile(fileName);
    }

    const links = tempLinks.links.map((d) => ({
      source: d["Source"],
      target: d["Target"],
    }));
    const nodes = tempNodes.nodes.map((d) => ({
      id: d["Id"],
      label: d["Label"],
      department: d["Department"],
      status: d["Status"],
      inDataset: d["In Dataset"],
      semesters: d["Semesters"],
      weight: d["Weight"],
      title: d["Title"],
      description: d["Description"],
      restrictions: d["Restrictions"],
      prerequisites: d["Prerequisites"],
      availability: d["availability"],
      capacity: d["capacity"],
      faculty: d["faculty"]
    }));

    const width = 1920,
      height = 1080;

    // Determines what happens when you drag a dot in the graph
    const drag = (simulation) => {
      function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      }

      function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
      }

      function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
      }

      return d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);
    };

    // Simulation code so that the graph itself is "active"
    const simulation = d3
      .forceSimulation(nodes)
      .force(
        "link",
        d3.forceLink(links).id((d) => d.id)
      )
      .force("radius", d3.forceCollide().radius(38))
      .force("charge", d3.forceManyBody().strength(-150))
      .force("center", d3.forceCenter(width / 2, height / 2));

    // Updates the area in the html code defined below
    const svg = d3.select("#area").attr("viewBox", [0, 0, width, height]);

    // Clears whatever is rendered in the SVG
    svg.selectAll("*").remove();

    // Append a div to house course info when a user hovers over a node
    d3.select('body')
      .append('div')
      .attr('id', 'tooltip')
      .attr('style', 'position: absolute; opacity: 0; padding:10px; max-width:400px; background:#0F3460; border:1px solid white;');

    // Styling for the edges of the graph between nodes
    const link = svg
      .append("g")
      .attr("stroke", "#999")
      .attr("stroke-opacity", 0.6)
      .selectAll("line")
      .data(links)
      .join("line")
      .attr("stroke-width", (d) => Math.sqrt(d.value));


    // Styling for the nodes
    const node = svg
      .append("g")
      .attr("stroke", "#fff")
      .attr("stroke-width", 1.5)
      .selectAll("circle")
      .data(nodes)
      .join("circle")
      .attr("r", 5)
      .style("fill", function (d) {
        let colour = colourDictionary[d.department];
        if (
          d.label.includes("NAW") === true ||
          d.label.includes("(Not in Dataset)") === true
        )
          return "#878787";
        else if (colour !== undefined) return colour;
        else return "#000000";
      })
      .call(drag(simulation));

    // Determining tooltip behaviour on mouseover, mousemove, and mouseout
    d3.select('#area').selectAll('circle').data(nodes)
      .join('circle')
      .attr('r', 3)
      .on('mouseover', function(e, d) {
        let textValue = "";
        
        if(d.title !== undefined) {
          textValue = "<b><u>" + d.title + "</u></b>";
        } else {
          textValue = "<b><u>Course Not Found Or Doesn't Exist</u></b>";
        }

        if(d.id !== undefined) {
          textValue = textValue + "<br><b>Course Code</b>: "+ d.id;
        }

        if(d.department !== undefined) {
          textValue = textValue + "<br><b>Department</b>: " + d.department;
        }

        if(d.description !== undefined) {
          textValue = textValue + "<br><b>Description</b>: " + d.description;
        }

        if(d.weight !== undefined) {
          textValue = textValue + "<br><b>Weight</b>: " + d.weight;
        }

        if(d.semesters !== undefined) {
          textValue = textValue + "<br><b>Semesters</b>: " + d.semesters;
        }

        if(d.availability !== undefined && d.capacity !== undefined) {
          textValue = textValue + "<br><b>Availability: </b>" + d.availability + "/" + d.capacity;
        }

        if(d.faculty !== undefined) {
          textValue = textValue + "<br><b>Faculty: </b>" + d.faculty;
        }

        if(d.restrictions !== undefined) {
          textValue = textValue + "<br><b>Restrictions</b>: " + d.restrictions;
        }

        if(d.prerequisites !== undefined) {
          textValue = textValue + "<br><b>Pre-reqs</b>: " + d.prerequisites;
        }
        
        d3.select('#tooltip')
          .style('opacity', 1)
          .style('z-index', 1)
          .html(textValue)
      })
      .on('mouseout', function(e) {
        d3.select('#tooltip').style('opacity', 0).style('z-index', -1)
      })
      .on('mousemove', function(e) {      
        d3.select('#tooltip').style('top', e.pageY-100+'px').style('left', e.pageX+10+'px')
      })

    // Fills the label information, assigns labels to nodes
    const label = svg
      .append("g")
      .attr("class", "label")
      .selectAll("text")
      .data(nodes)
      .enter()
      .append("text")
      .attr("dx", -25)
      .attr("dy", 25)
      .style("font-size", 6)
      .style("fill", d3.color("white"))
      .text(function (d) {
        return d.id;
      });

    simulation.on("tick", () => {
      link
        .attr("x1", (d) => d.source.x)
        .attr("y1", (d) => d.source.y)
        .attr("x2", (d) => d.target.x)
        .attr("y2", (d) => d.target.y);

      node.attr("cx", (d) => d.x).attr("cy", (d) => d.y);

      label
        .attr("x", function (d) {
          return d.x;
        })
        .attr("y", function (d) {
          return d.y;
        });
    });

    // Handle zooming calls
    svg.call(
      d3
        .zoom()
        .extent([
          [0, 0],
          [width * 3, height * 3],
        ])
        .on("zoom", zoomed)
    );

    // Zoom function which calls on all the parts of the graph to transform based on the zoom request
    function zoomed({ transform }) {
      node.attr("transform", transform);
      link.attr("transform", transform);
      label.attr("transform", transform);
    }

    return {
      nodes: () => {
        svg.node();
      },
    };
  } catch (e) {
    return;
  }
};

//This use effect happens on component mount and when the search state variable gets updated
//use an async function inside the use effect to call the api then update the state with
//course info

const GraphPage = ({ titleText }) => {
  const [exportGraph, exportData] = React.useState(false);
  const [exportGraphFromFile, setExportDataFromFile] = React.useState("");
  const [filterValues, setFilterValues] = React.useState({});
  const [allFiles, setAllFiles] = React.useState([]);
  const [selectedFile, setSelectedFile] = React.useState("");

  React.useEffect(() => {
    async function getFileNames() {
      let fileNames = await getAllExportFiles();
      fileNames = objToArray(fileNames);
      // Sort alphabetically, case insensitive
      fileNames = fileNames.sort(function (a, b) {
        return a.toLowerCase().localeCompare(b.toLowerCase());
      });
      setAllFiles(fileNames);
    }
    if (allFiles.length === 0) {
      getFileNames();
    }
  }, [allFiles]);

  React.useEffect(() => {
    async function makeGraph() {
      await createGraph("");
    }
    if (exportGraph === true) {
      makeGraph();
      setExportDataFromFile("nope");
    }
  }, [exportGraph]);

  React.useEffect(() => {
    const makeGraphFromFile = async (fileName) => {
      await createGraph(fileName);
    };
    if (exportGraphFromFile !== "nope") {
      exportData(false);
      makeGraphFromFile(exportGraphFromFile);
    }
  }, [exportGraphFromFile]);

  React.useEffect(() => {
    const filterData = async () => {
      let firstField = false;
      for (let i = 0; i < Object.keys(filterValues).length; i++) {
        if (
          Object.keys(filterValues)[i] === "courseCode" &&
          !!filterValues["courseCode"]
        ) {
          if (firstField !== false) {
            await filterSearchResults();
          }
          await getCourseCode(filterValues["courseCode"]);
          firstField = true;
        } else if (
          Object.keys(filterValues)[i] === "department" &&
          !!filterValues["department"]
        ) {
          if (firstField !== false) {
            await filterSearchResults();
          }
          await getAllCourseDepartments(filterValues["department"]);
          firstField = true;
        } else if (
          Object.keys(filterValues)[i] === "faculty" &&
          !!filterValues["faculty"]
        ) {
          if (firstField !== false) {
            await filterSearchResults();
          }
          await getAllCourseFaculty(filterValues["faculty"]);
          firstField = true;
        } else if (
          Object.keys(filterValues)[i] === "weights" &&
          filterValues["weights"].length !== 0
        ) {
          if (firstField !== false) {
            await filterSearchResults();
          }
          for (let i = 0; i < filterValues["weights"].length; i++) {
            await getAllCourseWeightData(filterValues["weights"][i]);
            if (i !== filterValues["weights"].length - 1) {
              await setUpCombineSearch();
            }
          }
          firstField = true;
        } else if (
          Object.keys(filterValues)[i] === "levels" &&
          filterValues["levels"].length !== 0
        ) {
          if (firstField !== false) {
            await filterSearchResults();
          }
          for (let i = 0; i < filterValues["levels"].length; i++) {
            await getAllCourseLevel(filterValues["levels"][i] / 1000);
            if (i !== filterValues["levels"].length - 1) {
              await setUpCombineSearch();
            }
          }
          firstField = true;
        } else if (
          Object.keys(filterValues)[i] === "availability" &&
          filterValues["availability"].length !== 0
        ) {
          if (firstField !== false) {
            await filterSearchResults();
          }
          for (let i = 0; i < filterValues["availability"].length; i++) {
            await getAllCourseAvailability(filterValues["availability"][i]);
            if (i !== filterValues["availability"].length - 1) {
              await setUpCombineSearch();
            }
          }
          firstField = true;
        }
      }
      if (exportGraph === true) {
        await exportData(false);
      }
      await exportData(true);
    };

    if (Object.keys(filterValues).length !== 0) {
      filterData();
    }
  }, [filterValues]);

  const handleFileSearch = (event) => {
    setSelectedFile(event.target.value);
  };

  return (
    <div>
      {exportGraph === false && exportGraphFromFile === "nope" ? (
        <div className="buttons-row">
          <RouteBox route="/search-courses">Search For Courses</RouteBox>
          <RouteBox key="export" onClick={() => exportData(true)}>
            Export From Recent Search
          </RouteBox>
          <select className="file-select" onChange={handleFileSearch}>
            {allFiles.map((str) => (
              <option key={str} value={str}>
                {str}
              </option>
            ))}
          </select>
          <RouteBox
            key="exportFromFile"
            onClick={() => setExportDataFromFile(selectedFile)}
          >
            Export From File
          </RouteBox>
        </div>
      ) : (
        <div>
          <div className="buttons-row">
            <RouteBox route="/search-courses">Search For Courses</RouteBox>
            <RouteBox key="export" onClick={() => exportData(true)}>
              Export From Recent Search
            </RouteBox>
            <select className="file-select" onChange={handleFileSearch}>
              {allFiles.map((str) => (
                <option key={str} value={str}>
                  {str}
                </option>
              ))}
            </select>
            <RouteBox
              key="exportFromFile"
              onClick={() => setExportDataFromFile(selectedFile)}
            >
              Export From File
            </RouteBox>
          </div>

          <div className="flex-panel-horizontal">
            <Panel sendDataUp={setFilterValues} filterValues={filterValues} />
            <svg id="area" className="graph-style"></svg>
          </div>
        </div>
      )}
    </div>
  );
};

export default GraphPage;
