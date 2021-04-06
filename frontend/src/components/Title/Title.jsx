import React from "react";
import "./Title.css";
import HomeIcon from "@material-ui/icons/Home";
import { Link } from "react-router-dom";

const Title = ({ titleText }) => {
  return (
    <div className="title-text title-div">
      <Link to="/decide-options" className="homeIcon">
        <div>
          <HomeIcon style={{ "font-size": "40px" }} />
        </div>
      </Link>
      {titleText}
    </div>
  );
};

export default Title;
