import React from "react";
import RouteBox from "./../../components/RouteBox";
import CourseList from "./../../components/CourseList";
import Loader from "./../../components/Loader";
import Button from "./../../components/Button";
import { getAllCourseSemester } from "./../../api-calls/lib.js";
import "./SemesterPage.css";

const SemesterPage = ({ titleText }) => {
  //This state will change when the user clicks on a card,
  //will cause the page to rerender showing course data
  const [search, setSearch] = React.useState("");
  const [searchData, setSearchData] = React.useState([]);
  const [selected, setSelected] = React.useState("");
  const searchVals = ["W", "S", "F"];

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

  //This use effect happens on component mount and when the search state variable gets updated
  //use an async function inside the use effect to call the api then update the state with
  //course info
  React.useEffect(
    function () {
      async function getCourseData() {
        let array = await getAllCourseSemester(search);
        setSearchData(array.courses);
      }
      if (search !== "") {
        getCourseData();
      }
    },
    [search]
  );

  return (
    <div className="search-courses-content">
      {search === "" ? (
        <React.Fragment>
          <h3>Choose a semester between winter, summer, or fall</h3>
          <div className="buttons-row">
            {/*Creates routeboxes so that user can select what weighting they want*/}
            {searchVals.map((str) => (
              <RouteBox
                selected={selected.includes(str)}
                key={str}
                onClick={() => addOrRemoveToState(str)}
              >
                {str}
              </RouteBox>
            ))}
          </div>
          <Button onClick={() => setSearch(selected)} height="5" width="50">
            search
          </Button>
        </React.Fragment>
      ) : (
        <div className="course-cards">
          {/*This section checks to see when the search data has been successfully
            pulled from the api and shows the loader while the user waits*/}
          {searchData.length === 0 ? (
            <Loader />
          ) : (
            <React.Fragment>
              <h2>Search returned {searchData.length} results</h2>
              <CourseList courseArray={searchData} />
            </React.Fragment>
          )}
        </div>
      )}
    </div>
  );
};

export default SemesterPage;
