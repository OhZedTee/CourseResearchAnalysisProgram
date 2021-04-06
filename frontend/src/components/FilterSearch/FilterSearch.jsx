import React from "react";
import "./FilterSearch.css";
import Button from "../Button";
import CourseList from "./../../components/CourseList";
import Loader from "./../../components/Loader";
import AutocompleteSearch from "./../../components/AutocompleteSearch";
import {
  allDepartments,
  weightOptions,
  levelOptions,
} from "./../../api-calls/consts.js";
import { objToArray } from "./../../api-calls/commonFuncs.js";

import {
  getAllCourseWeightData,
  getCourseCode,
  getAllCourseDepartments,
  getAllCourseFaculty,
  getAllCourseSemesterString,
  getAllCourseMaximum,
  getAllCourseMinimum,
  filterSearchResults,
  getAllUniqueCourseCodes,
  getAllFaculty,
  getAllCourseLevel,
} from "../../api-calls/lib";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const FilterSearch = ({ arrayToSearch = [] }) => {
  const [searchFaculty, setSearchFaculty] = React.useState([]);
  const [searchCodes, setSearchCodes] = React.useState([]);
  const [weightSearchBarContent, setWeightSearchBarContent] = React.useState(
    ""
  );
  const [
    departmentSearchBarContent,
    setDepartmentSearchBarContent,
  ] = React.useState("");
  const [semeterSearchBarContent, setSemesterSearchBarContent] = React.useState(
    ""
  );
  const [facultySearchBarContent, setFacultySearchBarContent] = React.useState(
    ""
  );
  const [levelSearchBarContent, setLevelSearchBarContent] = React.useState("");
  const [
    courseCodeSearchBarContent,
    setCourseCodeSearchBarContent,
  ] = React.useState("");
  const [
    capacityMaxSearchBarContent,
    setCapacityMaxSearchBarContent,
  ] = React.useState("");
  const [
    capacityMinSearchBarContent,
    setCapacityMinSearchBarContent,
  ] = React.useState("");
  const [searchData, setSearchData] = React.useState([]);
  const [isLoading, setIsLoading] = React.useState("not started");

  const handleFilterSearch = async (event) => {
    let array = [];
    setIsLoading("started");
    let firstField = false;

    for (let i = 0; i < arrayToSearch.length; ++i) {
      if (arrayToSearch[i] === "Course Weight" && !!weightSearchBarContent) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getAllCourseWeightData(weightSearchBarContent);
        firstField = true;
      } else if (
        arrayToSearch[i] === "Departments" &&
        !!departmentSearchBarContent
      ) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getAllCourseDepartments(departmentSearchBarContent);
        firstField = true;
      } else if (arrayToSearch[i] === "Semester" && !!semeterSearchBarContent) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getAllCourseSemesterString(semeterSearchBarContent);
        firstField = true;
      } else if (arrayToSearch[i] === "Faculty" && !!facultySearchBarContent) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getAllCourseFaculty(facultySearchBarContent);
        firstField = true;
      } else if (
        arrayToSearch[i] === "Course Code" &&
        !!courseCodeSearchBarContent
      ) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getCourseCode(courseCodeSearchBarContent);
        firstField = true;
      } else if (
        arrayToSearch[i] === "Capacity" &&
        !!capacityMinSearchBarContent
      ) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getAllCourseMinimum(capacityMinSearchBarContent);
        firstField = true;
      } else if (
        arrayToSearch[i] === "Capacity" &&
        !!capacityMaxSearchBarContent
      ) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getAllCourseMaximum(capacityMaxSearchBarContent);
        firstField = true;
      } else if (arrayToSearch[i] === "Levels" && !!levelSearchBarContent) {
        if (firstField !== false) {
          await filterSearchResults();
        }
        array = await getAllCourseLevel(levelSearchBarContent / 1000);
        firstField = true;
      }
    }

    setSearchData(array.courses);
    setIsLoading("finished");
  };

  React.useEffect(function () {
    async function getAllFacultyMembers() {
      let array = await getAllFaculty();
      setSearchFaculty(objToArray(array));
    }
    async function getAllCodes() {
      let array = await getAllUniqueCourseCodes();
      setSearchCodes(objToArray(array));
    }
    getAllFacultyMembers();
    getAllCodes();
  }, []);
  return (
    <React.Fragment>
      {searchData.length === 0 && isLoading === "not started" ? (
        <div className="search-courses-content">
          {arrayToSearch.includes("Course Weight") && (
            <div className="buttons-row-filter space-above max-width">
              Enter course weight (0.25, 0.50, 0.75. 1)
              <AutocompleteSearch
                currentVal={weightSearchBarContent}
                sendDataUp={setWeightSearchBarContent}
                suggestedVals={weightOptions}
              />
            </div>
          )}
          {arrayToSearch.includes("Levels") && (
            <div className="buttons-row-filter space-above max-width">
              Enter a course level (1000, 2000, 3000, 4000, 5000)
              <AutocompleteSearch
                currentVal={levelSearchBarContent}
                sendDataUp={setLevelSearchBarContent}
                suggestedVals={levelOptions}
              />
            </div>
          )}
          {arrayToSearch.includes("Departments") && (
            <div className="buttons-row-filter space-above max-width">
              Enter a department
              <AutocompleteSearch
                currentVal={departmentSearchBarContent}
                sendDataUp={setDepartmentSearchBarContent}
                suggestedVals={allDepartments}
              />
            </div>
          )}
          {arrayToSearch.includes("Semester") && (
            <div className="buttons-row-filter space-above max-width">
              Enter a semester (W, S, or F)
              <AutocompleteSearch
                currentVal={semeterSearchBarContent}
                sendDataUp={setSemesterSearchBarContent}
              />
            </div>
          )}
          {arrayToSearch.includes("Faculty") && (
            <div className="buttons-row-filter space-above max-width">
              Enter a professors name
              <AutocompleteSearch
                currentVal={facultySearchBarContent}
                sendDataUp={setFacultySearchBarContent}
                suggestedVals={searchFaculty}
              />
            </div>
          )}
          {arrayToSearch.includes("Course Code") && (
            <div className="buttons-row-filter space-above max-width">
              Enter a course code (example CIS*1500)
              <AutocompleteSearch
                currentVal={courseCodeSearchBarContent}
                sendDataUp={setCourseCodeSearchBarContent}
                suggestedVals={searchCodes}
              />
            </div>
          )}
          {arrayToSearch.includes("Capacity") && (
            <React.Fragment>
              <div className="buttons-row-filter space-above max-width">
                Enter a maximum capacity limit
                <AutocompleteSearch
                  currentVal={capacityMaxSearchBarContent}
                  sendDataUp={setCapacityMaxSearchBarContent}
                />
              </div>
              <div className="buttons-row-filter space-above max-width">
                Enter a minimum capacity limit
                <AutocompleteSearch
                  currentVal={capacityMinSearchBarContent}
                  sendDataUp={setCapacityMinSearchBarContent}
                />
              </div>
            </React.Fragment>
          )}
          <div className="buttons-row-filter space-above">
            <Button onClick={handleFilterSearch} height="5" width="150">
              Search
            </Button>
          </div>
        </div>
      ) : (
        <div className="course-cards">
          {/*This section checks to see when the search data has been successfully
            pulled from the api and shows the loader while the user waits*/}
          {isLoading === "started" ? (
            <Loader />
          ) : (
            <React.Fragment>
              <h2>{`Your search came back with ${searchData.length} courses`}</h2>
              <CourseList courseArray={searchData} />
            </React.Fragment>
          )}
        </div>
      )}
    </React.Fragment>
  );
};
export default FilterSearch;
