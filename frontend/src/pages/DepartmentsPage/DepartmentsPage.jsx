import React from "react";
import Loader from "./../../components/Loader";
import Button from "./../../components/Button";
import CourseList from "./../../components/CourseList";
import AutocompleteSearch from "./../../components/AutocompleteSearch";
import { getAllCourseDepartments } from "./../../api-calls/lib.js";
import { allDepartments } from "./../../api-calls/consts.js";
import "./DepartmentsPage.css";

const DepartmentsPage = ({ titleText }) => {
  //This state will change when the user clicks on a card,
  //will cause the page to rerender showing course data
  const [search, setSearch] = React.useState("");
  const [searchBarContent, setSearchBarContent] = React.useState("");
  const [searchData, setSearchData] = React.useState([]);
  const [noData, setNoData] = React.useState(false);

  //This use effect happens on component mount and when the search state variable gets updated
  //use an async function inside the use effect to call the api then update the state with
  //course info
  React.useEffect(
    function () {
      async function getCourseData() {
        let array = await getAllCourseDepartments(search);
        if (array.courses.length === 0) {
          setNoData(true);
        }
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
          <h3>Choose a department</h3>
          <div className="buttons-row">
            <AutocompleteSearch
              currentVal={searchBarContent}
              sendDataUp={setSearchBarContent}
              suggestedVals={allDepartments}
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

export default DepartmentsPage;
