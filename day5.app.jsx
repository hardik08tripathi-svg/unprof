import React from "react";
import ProfileCard from "./components/ProfileCard";
import "./App.css";

function App() {
  const worker = {
    name: "Rahul Sharma",
    profession: "Electrician",
    location: "Mumbai, Maharashtra",
    skills: ["Electrical Wiring", "Installation", "Maintenance", "Repair"],
    about:
      "Experienced electrician with over 5 years of expertise in residential and commercial electrical work.",
    image: "https://via.placeholder.com/150",
  };

  return (
    <div className="app">
      <ProfileCard worker={worker} />
    </div>
  );
}

export default App;
