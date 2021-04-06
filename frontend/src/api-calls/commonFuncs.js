export const objToArray = (obj) => {
  let newArray = [];
  Object.keys(obj).forEach((key) => {
    newArray.push(obj[key]);
  });
  return newArray;
};
