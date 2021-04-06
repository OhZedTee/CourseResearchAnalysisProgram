import React from "react";
import CourseCard from "./../CourseCard";
import Button from "./../Button";
import { setUpCombineSearch } from "./../../api-calls/lib.js";
import "./CourseList.css";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const CourseList = ({ courseArray }) => {
  return (
    <React.Fragment>
      <div className="flexbox-horizontal">
        <Button height="5" width="120" route="/graphs">
          Export Graph
        </Button>
        <Button
          onClick={() => setUpCombineSearch()}
          height="5"
          width="120"
          route="/search-courses"
        >
          Combine Data
        </Button>
        <Button height="5" width="120" route="/save-search">
          Save Search
        </Button>
      </div>
      {courseArray !== [] &&
        courseArray.map(
          ({
            weight,
            title,
            department,
            coursecode,
            description,
            restrictions,
            prereqs,
            status,
            availability,
            capacity,
            faculty,
          }) => (
            <div key={coursecode}>
              <CourseCard
                courseCode={coursecode}
                title={title}
                description={description}
                restrictions={restrictions}
                department={department}
                weight={weight}
                prereqs={prereqs}
                status={status}
                availability={availability}
                capacity={capacity}
                faculty={faculty}
              />
              <div className="space"></div>
            </div>
          )
        )}
    </React.Fragment>
  );
};
export default CourseList;
