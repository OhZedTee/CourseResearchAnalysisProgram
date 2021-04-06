import React from "react";
import "./Panel.css";
import AutocompleteSearch from "./../AutocompleteSearch";
import {
  getAllFaculty,
  getAllUniqueCourseCodes,
} from "./../../api-calls/lib.js";
import { allDepartments } from "./../../api-calls/consts.js";
import { objToArray } from "./../../api-calls/commonFuncs.js";
import Button from "./../Button";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const courseLevels = [1000, 2000, 3000, 4000, 5000];
const weights = ["0.25", "0.50", "0.75", "1.00"];
const availability = ["open", "closed", "all"];

const Panel = ({ sendDataUp, filterValues }) => {
  const [isHidden, setIsHidden] = React.useState(false);
  const [selectedLevels, setSelectedLevels] = React.useState(
    Object.keys(filterValues).length === 0 ? [] : filterValues["levels"]
  );
  const [selectedWeights, setSelectedWeights] = React.useState(
    Object.keys(filterValues).length === 0 ? [] : filterValues["weights"]
  );
  const [selectedAvailability, setSelectedAvailability] = React.useState(
    Object.keys(filterValues).length === 0 ? [] : filterValues["availability"]
  );
  const [selectedFaculty, setSelectedFaculty] = React.useState(
    Object.keys(filterValues).length === 0 ? "" : filterValues["faculty"]
  );
  const [selectedDepartment, setSelectedDepartment] = React.useState(
    Object.keys(filterValues).length === 0 ? "" : filterValues["department"]
  );
  const [selectedCode, setSelectedCode] = React.useState(
    Object.keys(filterValues).length === 0 ? "" : filterValues["courseCode"]
  );
  const [searchFaculty, setSearchFaculty] = React.useState([]);
  const [searchCodes, setSearchCodes] = React.useState([]);

  const returnData = () => {
    const obj = {
      levels: selectedLevels,
      weights: selectedWeights,
      availability: selectedAvailability,
      faculty: selectedFaculty,
      department: selectedDepartment,
      courseCode: selectedCode,
    };
    sendDataUp(obj);
  };

  const reset = () => {
    console.log("reset");
    setSelectedLevels([]);
    setSelectedWeights([]);
    setSelectedAvailability([]);
    setSelectedFaculty("");
    setSelectedDepartment("");
    setSelectedCode("");
  };

  React.useEffect(function () {
    async function getAllFacultyMembers() {
      let array = await getAllFaculty();
      let newArray = [];
      Object.keys(array).forEach((key) => {
        if (!newArray.includes(array[key])) {
          newArray.push(array[key]);
        }
      });

      setSearchFaculty(objToArray(newArray));
    }
    async function getAllCodes() {
      let array = await getAllUniqueCourseCodes();
      setSearchCodes(objToArray(array));
    }
    getAllFacultyMembers();
    getAllCodes();
  }, []);

  const addOrRemoveToLevels = (newState) => {
    let newArray = [...selectedLevels];
    if (!selectedLevels.includes(newState)) {
      newArray.push(newState);
    } else {
      const index = newArray.indexOf(newState);
      if (index > -1) {
        newArray.splice(index, 1);
      }
    }
    setSelectedLevels(newArray);
  };

  const addOrRemoveToWeights = (newState) => {
    let newArray = [...selectedWeights];
    if (!selectedWeights.includes(newState)) {
      newArray.push(newState);
    } else {
      const index = newArray.indexOf(newState);
      if (index > -1) {
        newArray.splice(index, 1);
      }
    }
    setSelectedWeights(newArray);
  };

  const addOrRemoveToAvailability = (newState) => {
    let newArray = [...selectedAvailability];
    if (!selectedAvailability.includes(newState)) {
      newArray.push(newState);
    } else {
      const index = newArray.indexOf(newState);
      if (index > -1) {
        newArray.splice(index, 1);
      }
    }
    setSelectedAvailability(newArray);
  };

  return (
    <React.Fragment>
      {isHidden ? (
        <div className="panel-hidden">
          <div
            className="hide-arrow-right"
            onClick={() => setIsHidden(!isHidden)}
          ></div>
        </div>
      ) : (
        <div className="flex-panel-vertical">
          <div
            className="hide-arrow-left"
            onClick={() => setIsHidden(!isHidden)}
          ></div>{" "}
          <h1 className="header-text-panel">SEARCH</h1>
          <h3 className="header-text-panel">Department</h3>
          <AutocompleteSearch
            currentVal={selectedDepartment}
            sendDataUp={setSelectedDepartment}
            suggestedVals={allDepartments}
          ></AutocompleteSearch>
          <h3 className="header-text-panel">Course Code</h3>
          <AutocompleteSearch
            currentVal={selectedCode}
            sendDataUp={setSelectedCode}
            suggestedVals={searchCodes}
          ></AutocompleteSearch>
          <h3 className="header-text-panel">Course Level</h3>
          <div className="radio-toolbar">
            {courseLevels.map((level) => (
              <Button
                width="35"
                height="10"
                selected={selectedLevels.includes(level)}
                onClick={() => addOrRemoveToLevels(level)}
                invert={false}
              >
                {level}
              </Button>
            ))}
          </div>
          <h3 className="header-text-panel">Course Weight</h3>
          <div className="radio-toolbar">
            {weights.map((level) => (
              <Button
                width="45"
                height="10"
                selected={selectedWeights.includes(level)}
                onClick={() => addOrRemoveToWeights(level)}
                invert={false}
              >
                {level}
              </Button>
            ))}
          </div>
          <h3 className="header-text-panel">Availability</h3>
          <div className="radio-toolbar">
            {availability.map((level) => (
              <Button
                width="55"
                height="10"
                selected={selectedAvailability.includes(level)}
                onClick={() => addOrRemoveToAvailability(level)}
                invert={false}
              >
                {level}
              </Button>
            ))}
          </div>
          <h3 className="header-text-panel">Faculty</h3>
          <AutocompleteSearch
            currentVal={selectedFaculty}
            sendDataUp={setSelectedFaculty}
            suggestedVals={searchFaculty}
          />
          <div className="flex-panel-horizontal">
            <Button width="125" invert={false} onClick={() => reset()}>
              Remove Filter
            </Button>
            <Button width="125" invert={false} onClick={() => returnData()}>
              Apply Changes
            </Button>
          </div>
        </div>
      )}
    </React.Fragment>
  );
};

export default Panel;
