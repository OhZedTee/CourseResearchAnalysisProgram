import React from "react";
import "./Loader.css";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const Loader = () => {
  return (
    <div className="spinner">
      <div></div>
      <div></div>
    </div>
  );
};
export default Loader;
