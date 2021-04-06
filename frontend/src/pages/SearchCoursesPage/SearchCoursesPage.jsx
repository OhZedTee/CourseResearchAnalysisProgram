import React from "react";
import RouteBox from "./../../components/RouteBox";
import Button from "./../../components/Button";
import FilterSearch from "./../../components/FilterSearch";
import "./SearchCoursesPage.css";

// This page shows the user all the metrics to search for and when the
// user clicks on one of the options will take them to the page (most pages not created yet)

const SearchCoursesPage = () => {
  const [selected, setSelected] = React.useState([]);
  const [searchCourses, setSearchCourses] = React.useState([]);

  const addOrRemoveToState = (newState) => {
    let newArray = [...selected];
    if (!selected.includes(newState)) {
      newArray.push(newState);
    } else {
      const index = newArray.indexOf(newState);
      if (index > -1) {
        newArray.splice(index, 1);
      }
    }
    setSelected(newArray);
  };

  const getRoute = () => {
    if (selected.length === 1) {
      let routeVal = selected[0];
      if (routeVal === "Course Weight") {
        return "/course-weight";
      } else if (routeVal === "Departments") {
        return "/departments";
      } else if (routeVal === "Semester") {
        return "/semesters";
      } else if (routeVal === "Faculty") {
        return "/faculty";
      } else if (routeVal === "Course Code") {
        return "/course-code";
      } else if (routeVal === "Capacity") {
        return "/Capacity";
      } else if (routeVal === "Levels") {
        return "/levels";
      }
    } else {
      return "";
    }
  };

  const startSearch = () => {
    setSearchCourses(selected);
  };

  return (
    <React.Fragment>
      {searchCourses.length === 0 ? (
        <div className="search-courses-content">
          <h3>What metric would you like to search for</h3>
          <div className="buttons-row">
            <RouteBox
              onClick={() => addOrRemoveToState("Course Weight")}
              selected={selected.includes("Course Weight")}
            >
              Course Weight
            </RouteBox>
            <RouteBox
              onClick={() => addOrRemoveToState("Departments")}
              selected={selected.includes("Departments")}
            >
              Departments
            </RouteBox>
            <RouteBox
              onClick={() => addOrRemoveToState("Semester")}
              selected={selected.includes("Semester")}
            >
              Semester
            </RouteBox>
            <RouteBox
              onClick={() => addOrRemoveToState("Levels")}
              selected={selected.includes("Levels")}
            >
              Levels
            </RouteBox>
          </div>
          <div className="buttons-row">
            <RouteBox
              onClick={() => addOrRemoveToState("Faculty")}
              selected={selected.includes("Faculty")}
            >
              Faculty
            </RouteBox>
            <RouteBox
              onClick={() => addOrRemoveToState("Course Code")}
              selected={selected.includes("Course Code")}
            >
              Course Code
            </RouteBox>
            <RouteBox
              onClick={() => addOrRemoveToState("Capacity")}
              selected={selected.includes("Capacity")}
            >
              Capacity
            </RouteBox>
          </div>
          <Button
            route={getRoute()}
            onClick={() => startSearch()}
            width={80}
            height={20}
          >
            Search
          </Button>
        </div>
      ) : (
        <React.Fragment>
          <FilterSearch arrayToSearch={searchCourses} />
        </React.Fragment>
      )}
    </React.Fragment>
  );
};

export default SearchCoursesPage;
