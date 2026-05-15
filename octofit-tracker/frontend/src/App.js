import React from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow-sm">
          <div className="container-fluid">
            <NavLink className="navbar-brand d-flex align-items-center" to="/">
              <img src="/octofitapp-small.svg" className="brand-logo me-2" alt="OctoFit Logo" />
              OctoFit Tracker
            </NavLink>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon" />
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
                <li className="nav-item">
                  <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/activities">
                    Activities
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/leaderboard">
                    Leaderboard
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/teams">
                    Teams
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/users">
                    Users
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/workouts">
                    Workouts
                  </NavLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <main className="app-main container">
          <div className="card mb-4 shadow-sm">
            <div className="card-body">
              <h1 className="card-title h4">OctoFit Tracker Dashboard</h1>
              <p className="card-text text-muted">
                Use the navigation menu to explore data from the backend REST API. Each view is styled with Bootstrap cards,
                tables, buttons, and modals for a consistent experience.
              </p>
              <div>
                <NavLink to="/activities" className="btn btn-primary btn-sm me-2">
                  View Activities
                </NavLink>
                <NavLink to="/leaderboard" className="btn btn-outline-primary btn-sm">
                  View Leaderboard
                </NavLink>
              </div>
            </div>
          </div>

          <Routes>
            <Route path="/" element={<Activities />} />
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="*" element={<Activities />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
