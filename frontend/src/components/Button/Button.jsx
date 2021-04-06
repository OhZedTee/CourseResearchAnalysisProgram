import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import "./Button.css";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const Button = ({
  onClick = () => {},
  width,
  height,
  route = "",
  selected = false,
  marginLeft = "0px",
  invert = true,
  children,
}) => {
  const ButtonStyle = styled.div`
    border: 1px solid black;
    background-color: ${selected ? "black" : "white"};
    width: ${width ? width + "px" : "80px"};
    height: ${height ? height + "px" : "20px"};
    overflow: hidden;
    text-decoration: none;
    color: ${selected ? "white" : "black"};
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-left: ${marginLeft};
    padding: 10px;
    font-size: 14px;
    &:hover {
      cursor: pointer;
      border: 2px solid black;
      width: ${width ? width - 2 + "px" : "78px"};
      height: ${height ? height - 2 + "px" : "18px"};
    }
  `;
  const InvertedButtonStyle = styled.div`
    border: 2px solid white;
    background-color: "black";
    width: ${width ? width + "px" : "80px"};
    height: ${height ? height + "px" : "20px"};
    overflow: hidden;
    text-decoration: none;
    color: "white";
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin-left: ${marginLeft};
    padding: 10px;
    font-size: 14px;
    &:hover {
      cursor: pointer;
      border: 4px solid white;
      color: "white";
      width: ${width ? width - 4 + "px" : "74px"};
      height: ${height ? height - 4 + "px" : "14px"};
    }
  `;
  return (
    <React.Fragment>
      {route === "" ? (
        <React.Fragment>
          {invert ? (
            <InvertedButtonStyle onClick={onClick}>
              <div>{children}</div>
            </InvertedButtonStyle>
          ) : (
            <ButtonStyle onClick={onClick}>
              <div>{children}</div>
            </ButtonStyle>
          )}
        </React.Fragment>
      ) : (
        <Link to={route} className="noDecorationsButton">
          <React.Fragment>
            {invert ? (
              <InvertedButtonStyle onClick={onClick}>
                <div>{children}</div>
              </InvertedButtonStyle>
            ) : (
              <ButtonStyle onClick={onClick}>
                <div>{children}</div>
              </ButtonStyle>
            )}
          </React.Fragment>
        </Link>
      )}
    </React.Fragment>
  );
};
export default Button;
