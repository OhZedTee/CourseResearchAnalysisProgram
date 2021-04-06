import React from "react";
import RouteBox from "./../../components/RouteBox";
import CourseList from "./../../components/CourseList";
import Loader from "./../../components/Loader";
import { getAllCourseLevel } from "./../../api-calls/lib.js";
import "./CourseLevelPage.css";

const CourseLevelPage = ({ titleText }) => {
  //This state will change when the user clicks on a card,
  //will cause the page to rerender showing course data
  const [search, setSearch] = React.useState("");
  const [searchData, setSearchData] = React.useState([]);
  const searchVals = ["1000", "2000", "3000", "4000", "5000"];

  //This use effect happens on component mount and when the search state variable gets updated
  //use an async function inside the use effect to call the api then update the state with
  //course info
  React.useEffect(
    function () {
      async function getCourseData() {
        let array = await getAllCourseLevel(search / 1000);
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
          <h3>Choose a course level</h3>
          <div className="buttons-row">
            {/*Creates routeboxes so that user can select what weighting they want*/}
            {searchVals.map((str) => (
              <RouteBox key={str} onClick={() => setSearch(str)}>
                {str}
              </RouteBox>
            ))}
          </div>
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

export default CourseLevelPage;
