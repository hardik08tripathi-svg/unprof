import React from "react";

function Skills({ skills }) {
  return (
    <div className="skills">
      <h3>Skills</h3>

      <div className="skill-list">
        {skills.map((skill, index) => (
          <span key={index} className="skill">
            {skill}
          </span>
        ))}
      </div>
    </div>
  );
}

export default Skills;
