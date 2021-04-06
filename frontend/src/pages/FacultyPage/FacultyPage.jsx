import React from "react";
import CourseList from "./../../components/CourseList";
import Loader from "./../../components/Loader";
import Button from "./../../components/Button";
import AutocompleteSearch from "./../../components/AutocompleteSearch";
import { getAllCourseFaculty, getAllFaculty } from "./../../api-calls/lib.js";
import { objToArray } from "./../../api-calls/commonFuncs.js";
import "./FacultyPage.css";

const FacultyPage = ({ titleText }) => {
  //This state will change when the user clicks on a card,
  //will cause the page to rerender showing course data
  const [search, setSearch] = React.useState("");
  const [searchData, setSearchData] = React.useState([]);
  const [searchFaculty, setSearchFaculty] = React.useState([]);
  const [searchBarContent, setSearchBarContent] = React.useState("");
  const [noData, setNoData] = React.useState(false);

  //This use effect happens on component mount and when the search state variable gets updated
  //use an async function inside the use effect to call the api then update the state with
  //course info
  React.useEffect(
    function () {
      async function getAllFacultyMembers() {
        let array = await getAllFaculty();
        setSearchFaculty(objToArray(array));
      }
      async function getCourseData() {
        let array = await getAllCourseFaculty(search);
        if (array.courses.length === 0) {
          setNoData(true);
        }
        setSearchData(array.courses);
      }
      if (search !== "") {
        getCourseData();
      }
      getAllFacultyMembers();
    },
    [search]
  );
  return (
    <div className="search-courses-content">
      {search === "" ? (
        <React.Fragment>
          <h3>Enter a professor to search for</h3>
          <div className="buttons-row">
            <AutocompleteSearch
              currentVal={searchBarContent}
              sendDataUp={setSearchBarContent}
              suggestedVals={searchFaculty}
            />
            <Button
              onClick={() => setSearch(searchBarContent)}
              marginLeft="15px"
              height="5"
              width="50"
            >
              search
            </Button>
          </div>
        </React.Fragment>
      ) : (
        <div className="course-cards">
          {/*This section checks to see when the search data has been successfully
              pulled from the api and shows the loader while the user waits*/}
          {searchData.length === 0 && !noData ? (
            <Loader />
          ) : (
            <React.Fragment>
              <h2>Search returned {searchData.length} results</h2>
              <CourseList courseArray={searchData} />
            </React.Fragment>
          )}
          {noData && <div>No Course Found</div>}
        </div>
      )}
    </div>
  );
};

export default FacultyPage;
