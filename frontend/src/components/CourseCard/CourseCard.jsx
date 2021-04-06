import React from "react";
import "./CourseCard.css";

// This class takes in course code, title, description, offerings, restrictions,
// and departments, and creates a card similar to the webadvisor course cards
// to display on the app

const CourseCard = ({
  courseCode = "",
  title = "",
  description = "",
  offerings = "",
  restrictions = "",
  department = "",
  weight = "",
  prereqs = "",
  status = "",
  availability = "",
  capacity = "",
  faculty = "",
}) => {
  return (
    <div className="course-card">
      <div className="course-card-title">{`${courseCode} ${title}`}</div>
      <div className="course-description">{description}</div>
      {offerings !== "" && (
        <div className="course-section">
          <div className="course-section-title">{`Offering(s):`}</div>
          <div className="course-section-content">{offerings}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {restrictions !== "" && (
        <div className="course-section">
          <div className="course-section-title">Restriction(s):</div>
          <div className="course-section-content">{restrictions}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {department !== "" && (
        <div className="course-section">
          <div className="course-section-title">Department(s):</div>
          <div className="course-section-content">{department}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {weight !== "" && (
        <div className="course-section">
          <div className="course-section-title">Weight:</div>
          <div className="course-section-content">{weight}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {prereqs !== "" && (
        <div className="course-section">
          <div className="course-section-title">Prerequisite(s):</div>
          <div className="course-section-content">{prereqs}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {status !== "" && (
        <div className="course-section">
          <div className="course-section-title">Status:</div>
          <div className="course-section-content">{status}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {availability !== "" && (
        <div className="course-section">
          <div className="course-section-title">Availability:</div>
          <div className="course-section-content">{availability}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {capacity !== "" && (
        <div className="course-section">
          <div className="course-section-title">Capacity:</div>
          <div className="course-section-content">{capacity}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
      {faculty !== "" && (
        <div className="course-section">
          <div className="course-section-title">Faculty:</div>
          <div className="course-section-content">{faculty}</div>
          <div>{/*spacing div, do not remove*/}</div>
        </div>
      )}
    </div>
  );
};

export default CourseCard;
