import React from "react";
import RouteBox from "./../../components/RouteBox";
import "./DecisionPage.css";

// This page lets the user select either search for courses or view graphs

const DecisionPage = ({ titleText }) => {
  return (
    <div className="decision-content">
      <h3>What would you like to use the app for</h3>
      <div className="buttons-row">
        <RouteBox route="/search-courses">Search For Courses</RouteBox>
        <RouteBox route="/graphs">View Graphs</RouteBox>
      </div>
    </div>
  );
};

export default DecisionPage;
