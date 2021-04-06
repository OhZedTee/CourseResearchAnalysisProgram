import React from "react";
import "./Slider.css";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const Slider = ({ handleSlideChange, max, min }) => {
  return (
    <input type="range" min={min} max={max} onChange={handleSlideChange} />
  );
};
export default Slider;
