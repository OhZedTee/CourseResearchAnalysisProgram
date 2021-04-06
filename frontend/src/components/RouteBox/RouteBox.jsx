import React from "react";
import { Link } from "react-router-dom";
import "./RouteBox.css";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const RouteBox = ({
  route = "",
  onClick = () => {},
  selected = false,
  children,
}) => {
  return (
    <React.Fragment>
      {route === "" ? (
        <React.Fragment>
          {selected ? (
            <div onClick={onClick} className="icon-box-selected">
              <div>{children}</div>
            </div>
          ) : (
            <div onClick={onClick} className="icon-box">
              <div>{children}</div>
            </div>
          )}
        </React.Fragment>
      ) : (
        <Link to={route} className="icon-box">
          <div>{children}</div>
        </Link>
      )}
    </React.Fragment>
  );
};
export default RouteBox;
