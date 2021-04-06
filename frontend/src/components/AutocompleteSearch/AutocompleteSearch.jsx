import React from "react";
import "./AutocompleteSearch.css";

// This class creates a card with text on it that can either bring user to the main
// page or you can pass in a function that will run when the user clicks on it

const AutocompleteSearch = ({
  currentVal = "",
  sendDataUp = () => {},
  suggestedVals = [],
}) => {
  const [value, setValue] = React.useState(currentVal);
  const [suggestions, setSuggestions] = React.useState([]);
  const [valid, setValid] = React.useState(true);

  if (value !== currentVal) {
    setValue(currentVal);
  }

  const checkValid = () => {
    if (suggestedVals.length !== 0) {
      let isTrue = false;
      suggestedVals.forEach((val) => {
        if (val) {
          if (val.toLowerCase().includes(value.toLowerCase())) {
            isTrue = true;
          }
          if (val.toLowerCase() === value.toLowerCase()) {
            setSuggestions([]);
          }
        }
      });
      setValid(isTrue);
    }
  };

  React.useEffect(
    function () {
      async function getSuggestions() {
        await setSuggestions([]);
        if (value !== "") {
          let array = [];
          suggestedVals.forEach((val) => {
            if (
              val.toLowerCase().includes(value.toLowerCase()) &&
              val !== value &&
              val[0].toLowerCase() === value[0].toLowerCase()
            ) {
              if (!array.includes(val)) {
                array.push(val);
              }
            }
            let tempStr = val.split(" ");
            if (tempStr.length > 1) {
              if (
                tempStr[1][0] &&
                value[0] &&
                tempStr[1][0].toLowerCase() === value[0].toLowerCase() &&
                tempStr[1].toLowerCase().includes(value.toLowerCase())
              ) {
                if (!array.includes(val)) {
                  array.push(val);
                }
              }
            }
          });
          setSuggestions(array);
        } else {
          setSuggestions([]);
        }
      }
      getSuggestions();
    },
    [value]
  );

  const handleChange = (event) => {
    sendDataUp(event.target.value);
    setValue(event.target.value);
    checkValid();
  };

  const setValueAndPassUp = (newVal) => {
    sendDataUp(newVal);
    setValue(newVal);
  };

  return (
    <React.Fragment>
      {valid ? (
        <div className="searchBarFlex">
          <input
            className="search-bar"
            type="text"
            value={value}
            onChange={handleChange}
          />
          <Suggestions
            suggestedVals={suggestions}
            setValue={setValueAndPassUp}
          />
        </div>
      ) : (
        <div className="searchBarFlex invalid">
          <input
            className="search-bar invalid"
            type="text"
            value={value}
            onChange={handleChange}
          />
          <Suggestions
            suggestedVals={suggestions}
            setValue={setValueAndPassUp}
          />
        </div>
      )}
    </React.Fragment>
  );
};

const Suggestions = ({ suggestedVals = [], setValue = () => {} }) => {
  return (
    <React.Fragment>
      {suggestedVals.length !== 0 && (
        <div>
          {suggestedVals.map((val) => (
            <div className="options" key={val} onClick={() => setValue(val)}>
              {val}
            </div>
          ))}
        </div>
      )}
    </React.Fragment>
  );
};
export default AutocompleteSearch;
