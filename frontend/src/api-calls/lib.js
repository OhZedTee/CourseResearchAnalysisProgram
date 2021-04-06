import axios from "axios";

// We should look into setting dev flags for when we run "npm start"
// There are some built in, like process.env.NODE_ENV

let header = "";
let port = "";

if (process.env.REACT_APP_ENV === "production") {
  header = "http://cis4250-02.socs.uoguelph.ca";
  port = "80";
} else {
  header = "http://127.0.0.1";
  port = "5000";
}

export const getAllCourseWeightData = async (courseWeight) => {
  let array = await axios
    .get(`${header}:${port}/find/weight?term=${courseWeight}`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));

  return array;
};

export const getAllExportFiles = async () => {
  let returnVal = await axios
    .get(`${header}:${port}/get/exportFiles`)
    .then((res) => {
      return res.data;
    });

  return returnVal;
};

export const exportSearchDataEdgesFromFile = async (filename) => {
  let edges = await axios
    .get(`${header}:${port}/get/edges?term=${filename}`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));

  return edges;
};

export const exportSearchDataNodesFromFile = async (filename) => {
  let nodes = await axios
    .get(`${header}:${port}/get/nodes?term=${filename}`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));

  return nodes;
};

export const exportSearchData = async (filename) => {
  axios
    .post(`${header}:${port}/export/${filename}`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));
};

export const exportSearchDataEdges = async () => {
  let edges = await axios
    .get(`${header}:${port}/exportEdges`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));

  return edges;
};

export const exportSearchDataNodes = async () => {
  let nodes = await axios
    .get(`${header}:${port}/exportNodes`)
    .then((res) => {
      return res.data;
    })
    .catch((error) => console.log(error));

  return nodes;
};

export const getCourseCode = async (courseCode) => {
  let array = await axios
    .get(`${header}:${port}/find/full_course_code?term=${courseCode}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseDepartments = async (department) => {
  let array = await axios
    .get(`${header}:${port}/find/department?term=${department}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseFaculty = async (facultyName) => {
  let array = await axios
    .get(`${header}:${port}/find/faculty?term=${facultyName}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseSemester = async (semesterArray) => {
  let semesterString = "";
  semesterArray.forEach((semester) => {
    semesterString = semesterString + semester + ",";
  });
  semesterString = semesterString.slice(0, -1);
  let array = await axios
    .get(`${header}:${port}/find/semester?term=${semesterString}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseSemesterString = async (semesterStr) => {
  let array = await axios
    .get(`${header}:${port}/find/semester?term=${semesterStr}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseMaximum = async (max) => {
  let array = await axios
    .get(`${header}:${port}/find/capacity_maximum?term=${max}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseLevel = async (level) => {
  let array = await axios
    .get(`${header}:${port}/find/level?term=${level}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseAvailability = async (availability) => {
  let array = await axios
    .get(`${header}:${port}/find/availability?term=${availability}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const getAllCourseMinimum = async (min) => {
  let array = await axios
    .get(`${header}:${port}/find/capacity_minimum?term=${min}`)
    .then((res) => {
      return res.data;
    });

  return array;
};

export const filterSearchResults = async () => {
  let array = await axios.put(`${header}:${port}/multi/filter`).then((res) => {
    return res.data;
  });

  return array;
};

export const setUpCombineSearch = async () => {
  let returnVal = await axios
    .put(`${header}:${port}/multi/combine`)
    .then((res) => {
      return res.data;
    });

  return returnVal;
};

export const getAllFaculty = async () => {
  let returnVal = await axios
    .get(`${header}:${port}/get/faculty`)
    .then((res) => {
      return res.data;
    });

  return returnVal;
};

export const getAllUniqueCourseCodes = async () => {
  let returnVal = await axios
    .get(`${header}:${port}/get/allCourseCodes`)
    .then((res) => {
      return res.data;
    });

  return returnVal;
};
