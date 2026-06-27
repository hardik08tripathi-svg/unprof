import React from "react";
import ProfileImage from "./ProfileImage";
import Skills from "./Skills";

function ProfileCard({ worker }) {
  return (
    <div className="profile-card">
      <ProfileImage image={worker.image} />

      <h2>{worker.name}</h2>

      <h4>{worker.profession}</h4>

      <p className="location">📍 {worker.location}</p>

      <Skills skills={worker.skills} />

      <div className="about">
        <h3>About</h3>
        <p>{worker.about}</p>
      </div>

      <button className="connect-btn">
        Connect
      </button>
    </div>
  );
}

export default ProfileCard;
