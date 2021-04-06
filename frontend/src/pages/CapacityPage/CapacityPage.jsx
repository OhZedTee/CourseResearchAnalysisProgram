import React from "react";
import RouteBox from "./../../components/RouteBox";
import CourseList from "./../../components/CourseList";
import Loader from "./../../components/Loader";
import Button from "./../../components/Button";
import Slider from "./../../components/Slider";
import {
  getAllCourseMaximum,
  getAllCourseMinimum,
} from "./../../api-calls/lib.js";
import "./CapacityPage.css";

const CapacityPage = ({ titleText }) => {
  //This state will change when the user clicks on a card,
  //will cause the page to rerender showing course data
  const [search, setSearch] = React.useState("");
  const [selected, setSelected] = React.useState([]);
  const [sliderVal, setSliderVal] = React.useState(10);
  const [searchData, setSearchData] = React.useState([]);

  const handleSlideChange = (event) => {
    setSliderVal(event.target.value);
  };

  //This use effect happens on component mount and when the search state variable gets updated
  //use an async function inside the use effect to call the api then update the state with
  //course info
  React.useEffect(
    function () {
      async function getCourseData() {
        let array = [];
        if (selected === "Max") {
          array = await getAllCourseMaximum(sliderVal);
        } else if (selected === "Min") {
          array = await getAllCourseMinimum(sliderVal);
        }

        if (array.courses) {
          setSearchData(array.courses);
        } else {
          setSearchData([]);
        }
      }
      if (search !== "") {
        getCourseData();
      }
    },
    [search, selected, sliderVal]
  );

  return (
    <div className="search-courses-content">
      {search === "" ? (
        <React.Fragment>
          <h3>Select a capacity</h3>
          <Slider handleSlideChange={handleSlideChange} max="500" min="10" />
          {sliderVal}
          <div className="buttons-row space-above">
            <RouteBox
              onClick={() => setSelected("Max")}
              selected={selected.includes("Max")}
            >
              Max
            </RouteBox>
            <RouteBox
              onClick={() => setSelected("Min")}
              selected={selected.includes("Min")}
            >
              Min
            </RouteBox>
          </div>
          <Button onClick={() => setSearch(sliderVal)} height="5" width="50">
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

export default CapacityPage;
