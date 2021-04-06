import React from "react";
import "./SaveExportFilePage.css";
import Button from "./../../components/Button";
import { exportSearchData } from "./../../api-calls/lib.js";
import { Link } from "react-router-dom";

// This page lets users save their recent search as a file on the server

const SaveExportFilePage = ({ titleText }) => {
  
  const [save, setSave] = React.useState("");
  const [fileNameContent, setFileNameContent] = React.useState("");

  React.useEffect(
    function () {
      async function saveSearch(fileName) {
        await exportSearchData(fileName);
      }
      saveSearch(save);
    }, [save]);

  const handleSave = (event) => {
    setFileNameContent(event.target.value);
  };

  return (
    <div>
      {save === "" ? (
        <div className="decision-content">
          <h3>Please enter a file name to save the search as</h3>
          <div className="search-courses-content">
            <div className="buttons-row-filter space-above max-width">
              File Name
              <div className="searchBarFlex">
                <input
                  className="search-bar"
                  type="text"
                  value={fileNameContent}
                  onChange={handleSave}
                />
              </div>
                <Button
                  onClick={() => setSave(fileNameContent)}
                  height="5"
                  width="100"
                >
                    Save Search
                </Button>
            </div>
          </div>
        </div>
      ) : (
        <div className="decision-content">
          <h3>Search saved! Click the button below to view your search as a graph</h3>
          <Link to={"/graphs"} className="noDecorationsButton">
            <Button height="5" width="120">
              View Graph
            </Button>
          </Link>
        </div>
      )}
    </div>
  );
};

export default SaveExportFilePage;
