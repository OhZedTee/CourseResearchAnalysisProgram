import React from "react";
import Title from "./components/Title";
import RouteBox from "./components/RouteBox";
import DecisionPage from "./pages/DecisionPage";
import SearchCoursesPage from "./pages/SearchCoursesPage";
import CourseWeightPage from "./pages/CourseWeightPage";
import DepartmentsPage from "./pages/DepartmentsPage";
import SemesterPage from "./pages/SemesterPage";
import FacultyPage from "./pages/FacultyPage";
import CourseCodePage from "./pages/CourseCodePage";
import CapacityPage from "./pages/CapacityPage";
import GraphPage from "./pages/GraphPage";
import SaveExportFilePage from "./pages/SaveExportFilePage";
import CourseLevelPage from "./pages/CourseLevelPage";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./index.css";

export default function BasicExample() {
  return (
    <Router>
      <div className="main-page">
        <Title titleText="Course Research Analysis Program" />
        {/* <Component route="/pageUrlHere" />*/}
        {/*
          A <Switch> looks through all its children <Route>
          elements and renders the first one whose path
          matches the current URL. Use a <Switch> any time
          you have multiple routes, but you want only one
          of them to render at a time
        */}
        <Switch>
          {/*
            These routes will render different components based on the url path
            */}
          <Route exact path="/">
            <MainPage />
          </Route>
          <Route exact path="/decide-options">
            <DecisionPage />
          </Route>
          <Route exact path="/search-courses">
            <SearchCoursesPage />
          </Route>
          <Route exact path="/course-weight">
            <CourseWeightPage />
          </Route>
          <Route exact path="/graphs">
            <GraphPage />
          </Route>
          <Route exact path="/departments">
            <DepartmentsPage />
          </Route>
          <Route exact path="/semesters">
            <SemesterPage />
          </Route>
          <Route exact path="/faculty">
            <FacultyPage />
          </Route>
          <Route exact path="/course-code">
            <CourseCodePage />
          </Route>
          <Route exact path="/capacity">
            <CapacityPage />
          </Route>
          <Route exact path="/save-search">
            <SaveExportFilePage />
          </Route>
          <Route exact path="/levels">
            <CourseLevelPage />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

const MainPage = () => {
  return (
    <React.Fragment>
      <div className="content">
        <div className="page-description">
          Welcome to the University of Guelph Course Research Analysis Program,
          CRAP for short. To get started, we need you to provide the filename to
          the dataset in the main directory. For more information, click the
          link
          <a href="https://git.socs.uoguelph.ca/team2-design5/project/-/wikis/Data-Set-Generation">
            {" "}
            here
          </a>
        </div>
        <RouteBox route="/decide-options">Enter Website</RouteBox>
      </div>
    </React.Fragment>
  );
};
